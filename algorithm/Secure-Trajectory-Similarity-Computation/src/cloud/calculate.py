#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhan Shi
Time  : 2021/5/12 14:03
"""
import tqdm
from colorama import Fore

from src.cloud.protocol import phe_protocol
from src.cloud.protocol import sspld
from src.util.timer import timer


def calculating(pk, filtered_dataset, query_point, length_true, path, dmax):
    """
    Calculating using filtered trajectory dataset and query trajectory
    :param pk: PHE public key
    :param filtered_dataset: filtered trajectory dataset
    :param query_point: point of query trajectory
    :param length_true: the true length
    :param path: path of trajectory dataset
    :param dmax: the allowed maximum distance
    :return: cost time
    """
    distance_1 = [[] for _ in range(len(filtered_dataset))]
    distance_2 = distance_1.copy()
    large = pk.encrypt(pk.n & 0xffffff)
    for i in range(len(filtered_dataset)):
        phi = [0 for _ in range(len(filtered_dataset[i]))]
        theta = []
        for j in range(len(filtered_dataset[i])):
            phi[j] = large
            for k in range(len(query_point) - 1):
                theta.append(sspld.phe_sspld(pk, filtered_dataset[i][j], query_point[k], query_point[k + 1]))
                phi[j] = phe_protocol.PHEProtocol(phi[j]).phe_min(theta[k])

        distance_1[i] = [0 for _ in range(len(filtered_dataset[i]))]
        for j in range(len(filtered_dataset[i])):
            distance_1[i][j] = phe_protocol.PHEProtocol(phi[j]).phe_mul(length_true[i][j])

        theta = [0]
        distance_2[i] = [0 for _ in range(len(query_point))]
        for j in range(len(query_point)):
            distance_2[i][j] = large
            for k in range(len(filtered_dataset[i]) - 1):
                theta.append(sspld.phe_sspld(pk, query_point[i], filtered_dataset[i][k], filtered_dataset[i][k + 1]))
                distance_2[i][j] = phe_protocol.PHEProtocol(distance_2[i][j]).phe_min(theta[k])

    similarity = [0 for _ in range(len(filtered_dataset))]
    # for i in tqdm.tqdm(range(len(filtered_dataset)), desc=f"{Fore.YELLOW}Calculate result of the similarity"):
    for i in range(len(filtered_dataset)):
        gamma = sum(distance_1[i]) + sum(distance_2[i])
        lamb = sum(length_true[i]) + pk.encrypt(len(query_point) + 1)
        similarity[i] = phe_protocol.PHEProtocol(gamma).phe_truediv(lamb)

    return "COM", path, str(len(filtered_dataset)), dmax, similarity
