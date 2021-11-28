#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhan Shi
Time  : 2021/5/12 14:03
"""
import random

import pandas as pd
import phe

import keypair


def phe_stfsm(pk, sgs, tgs):
    """
    Secure Trajectory Filtering Signature Matching
    :param pk: public key
    :param sgs: survey grid signature
    :param tgs: trajectory grid signature
    :return: matching mark
    """
    omega = list()
    for i in range(len(sgs)):
        omega.append([])
        for j in range(len(sgs[i])):
            omega[i].append([])
            for k in range(len(tgs)):
                r = random.SystemRandom().randrange(1, pk.n & 0xffffff)
                omega[i][j].append((sgs[i][j] - tgs[k]) * r)

    epsilon = phe_third_stfsm(omega, pk)
    sigma = sum(epsilon)

    return sigma


def phe_third_stfsm(w, pk):
    """
    Secure Trajectory Filtering Signature Matching
    :param w: omega
    :param pk: public key
    :return: matching result
    """
    private_key = pd.read_pickle(keypair.PRIVATE_KEY_PATH)
    sk = phe.PaillierPrivateKey(p=int(private_key.loc['p'][0]),
                                public_key=pk, q=int(private_key.loc['q'][0]))

    epsilon = []
    for i in range(len(w)):
        epsilon.append(pk.encrypt(1))
        for j in range(len(w[i])):
            for k in range(len(w[i][j])):
                if sk.decrypt(w[i][j][k]) == 0:
                    epsilon[i] = 0
                    break
            if epsilon[i] == 0:
                epsilon[i] = pk.encrypt(0)
                break

    return epsilon
