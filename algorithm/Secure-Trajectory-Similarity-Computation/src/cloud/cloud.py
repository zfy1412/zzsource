#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhan Shi
Time  : 2021/5/7 12:13
"""
import logging as log
import random

import numpy as np
import pandas as pd
import phe
import tqdm
from colorama import Fore

import keypair
from src.cloud import calculate, match
from src.util.timer import timer



def cloud(cnt, path, dmax):
    """
    Cloud
    :param n: number of trajectories in trajectory dataset
    :param path: path of trajectory dataset
    :param dmax: the allowed maximum distance
    :return: some params
    """
    pk = phe.PaillierPublicKey(n=int(pd.read_pickle(keypair.PUBLIC_KEY_PATH).loc['n'][0]))
    leng=len(cnt)
    query_name = f"{path}_query_{dmax}.pkl"
    # query_name = f"{path}_{str(1).zfill(5)}_{dmax}.pkl"
    query = pd.read_pickle(f"encryption/query/{dmax}/{query_name}")
    # query = pd.read_pickle(f"encryption/normal/{dmax}/{query_name}")
    query_tgs = [tg for tg in query.loc['tg'] if tg is not None]
    query_sgs = [sg for sg in query.loc['sg'] if sg is not None]
    query_point = [p for p in query.loc['p'] if p is not None]

    dataset = list()

    for i in range(0, leng):
        file_name = f"{path}_{str(cnt[i]).zfill(5)}_{dmax}.pkl"
        dataset.append(pd.read_pickle(f"encryption/{path}/{dmax}/{file_name}"))

    result_matching = match.matching(pk, cnt, path, dmax, dataset, [query_name, query_tgs, query_sgs])
    filtered_dataset = result_matching[4]
    length_true = result_matching[5]

    result_calculating = calculate.calculating(pk, filtered_dataset, query_point, length_true, path, dmax)
    result_sim = result_calculating[4]

    random_numbers = [random.SystemRandom().randrange(1, pk.n & 0xffffff) for _ in range(len(result_sim))]
    random_sim = phe_third_result_decrypt([result_sim[i] + random_numbers[i]
                                           for i in range(len(result_sim))], pk)

    similarity = np.array([round(random_sim[i] - random_numbers[i], 2) for i in range(len(random_sim))])

    filtered_len = len(filtered_dataset)
    number_unfiltered = len(filtered_dataset[0]) if len(filtered_dataset) > 0 else 0

    file_handle_result = log.FileHandler("log/result.log", 'a', encoding='utf-8')
    file_handle_result.setFormatter(log.Formatter(fmt="%(asctime)s %(message)s"))
    logger_result = log.Logger('', level=log.INFO)
    logger_result.addHandler(file_handle_result)
    if len(similarity)==0:
        print(0xffffff)
    else:
        print(similarity[0])
    dataset_name = ("NOR" if path == "normal" else
                    "UNI" if path == "uniform" else
                    "SHH" if path == "SHH-Taxi" else
                    "TDR" if path == "T-drive" else '')
    logger_result.info('\n'
                       f"1  Num.  of  Trajectory     {cnt}\n"
                       f"2  Nam.  of  Dataset  T     {dataset_name}\n"
                       f"3  Dmx.  of  Processing     {dmax.rjust(3, ' ')}\n"
                       f"4  Num.  of  Dealed   T     {str(filtered_len).rjust(3, ' ')}\n"
                       f"5  Len.  of  Dealed   T     {str(number_unfiltered).rjust(3, ' ')}\n"
                       f"6  Sim.  of  Processing     {similarity}")

    return "CLD", path, cnt, dmax


def phe_third_result_decrypt(result, pk):
    """
    Decrypt result of similarity
    :param result: random encrypted result
    :param pk: the public key
    :return: decrypted random encrypted result
    """
    private_key = pd.read_pickle(keypair.PRIVATE_KEY_PATH)
    sk = phe.PaillierPrivateKey(p=int(private_key.loc['p'][0]),
                                public_key=pk, q=int(private_key.loc['q'][0]))

    return [sk.decrypt(v) for v in result]
