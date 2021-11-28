#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhan Shi
Time  : 2021/5/12 14:03
"""
import tqdm
from colorama import Fore

from src.cloud.matrix import construct, filter
from src.cloud.protocol import stfsm
from src.util.timer import timer



def matching(pk, cnt, path, dmax, dataset, query):
    """
    Matching using Grid Signature
    :param pk: PHE public key
    :param n: number of trajectories in trajectory dataset
    :param path: path of trajectory dataset
    :param dmax: the allowed maximum distance
    :param dataset: trajectory dataset
    :param query: query trajectory
    :return: cost time
    """
    (query_name, query_tgs, query_sgs) = query
    leng=len(cnt)
    sigma = list()

    for i in range(0, leng):
        file_name = f"{path}_{str(cnt[i]).zfill(5)}_{dmax}.pkl"

        dataset_sgs = [sg for sg in dataset[i].loc['sg'] if sg is not None]
        dataset_tgs = [tg for tg in dataset[i].loc['tg'] if tg is not None]
        sigma.append(stfsm.phe_stfsm(pk, query_sgs, dataset_tgs) + stfsm.phe_stfsm(pk, dataset_sgs, query_tgs))

    recovery_matrix = construct.construct_filter_matrix(pk, sigma)

    dataset_true = list()
    length_true = list()
    for i in range(len(dataset)):
        dataset_true.append([data for data in dataset[i].loc['p'] if data is not None])
        length_true.append([length for length in dataset[i].loc['l'] if length is not None])

    filtered_dataset, filtered_length = filter.matrix_filter(dataset_true, length_true, recovery_matrix)

    return "MAT", path, cnt, dmax, filtered_dataset, filtered_length
