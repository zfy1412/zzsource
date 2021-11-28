#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhan Shi
Time  : 2021/5/12 14:04
"""
import random

import numpy as np
import pandas as pd
import phe
import tqdm
from colorama import Fore

import keypair


def construct_filter_matrix(pk, sigma):
    """
    Construct filtering matrix
    :param pk: the public key
    :param sigma: filtering mark
    :return: filtering matrix
    """
    r = [random.SystemRandom().randrange(1, pk.n & 0xffffff) for _ in sigma]
    eta = np.multiply(np.array(sigma), np.array(r))
    # out of order
    pi = list(range(len(eta)))
    random.shuffle(pi)
    sorted_eta = [eta[pi[i]] for i in range(len(eta))]

    shorted_matrix = phe_third_construct_filter_matrix(sorted_eta, pk)

    # restore order
    recovery_matrix = np.zeros_like(shorted_matrix)
    for i in range(len(shorted_matrix)):
        for j in range(len(shorted_matrix[i])):
            recovery_matrix[i][pi[j]] = shorted_matrix[i][j]

    return recovery_matrix


def phe_third_construct_filter_matrix(shorted_eta, pk):
    """
    Construct Filtering Matrix
    :param shorted_eta: eta of out of order
    :param pk: the public key
    :return: Filtering Matrix
    """
    private_key = pd.read_pickle(keypair.PRIVATE_KEY_PATH)
    sk = phe.PaillierPrivateKey(p=int(private_key.loc['p'][0]),
                                public_key=pk, q=int(private_key.loc['q'][0]))

    f = 0
    matrix = list()
    # for i in tqdm.tqdm(range(len(shorted_eta)), desc=f"{Fore.YELLOW}Creating Filtering Matrix"):
    for i in range(len(shorted_eta)):
        if sk.decrypt(shorted_eta[i]) == 0:
            matrix.append([pk.encrypt(0) for _ in range(len(shorted_eta))])
            matrix[f][i] = pk.encrypt(1)
            f += 1

    return matrix
