#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhan Shi
Time  : 2021/5/12 14:04
"""
import tqdm
from colorama import Fore

from src.cloud.protocol import phe_protocol


def matrix_filter(dataset, length, matrix):
    """
    Computation of filtered trajectory using filtering matrix
    :param dataset: original trajectory dataset
    :param length: original trajectory length
    :param matrix: filtering matrix
    :return: filtered trajectory dataset
    """
    filtered_dataset = []
    filtered_length = []
    # for i in tqdm.tqdm(range(len(matrix)), desc=f"{Fore.YELLOW}Trajectories Filtering"):
    for i in range(len(matrix)):
        filtered_dataset.append([])
        filtered_length.append([])
        filtered_dataset[i] = [[0, 0] for _ in range(len(dataset[0]))]
        filtered_length[i] = [0 for _ in range(len(length[0]))]
        for j in range(len(dataset)):
            for k in range(len(dataset[j])):
                filtered_point_x = (filtered_dataset[i][k][0] +
                                    phe_protocol.PHEProtocol(dataset[j][k][0]).phe_mul(matrix[i][j]))
                filtered_point_y = (filtered_dataset[i][k][1] +
                                    phe_protocol.PHEProtocol(dataset[j][k][1]).phe_mul(matrix[i][j]))
                filtered_dataset[i][k] = [filtered_point_x, filtered_point_y]

                filtered_length[i][k] = (filtered_length[i][k] +
                                         phe_protocol.PHEProtocol(length[j][k]).phe_mul(matrix[i][j]))

    return filtered_dataset, filtered_length
