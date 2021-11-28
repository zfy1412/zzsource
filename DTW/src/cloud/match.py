#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhao Fanyou
Time  : 2021/11/9 20:42
"""
import phe
import keypair
import pandas as pd
from src.cloud.protocol import phe_protocol
import numpy as np

def dtw_distance(ts_a, ts_b):
    """
    DTW algorithm
    :param ts_a: the point set one
    :param ts_b: the point set two

    """
    mww = 100000000000
    ts_a, ts_b = np.array(ts_a), np.array(ts_b)
    M, N = len(ts_a), len(ts_b)
    pk = phe.PaillierPublicKey(n=int(pd.read_pickle(keypair.PUBLIC_KEY_PATH).loc['n'][0]))
    cost = [[pk.encrypt(mww) for _ in range(N)]for _ in range(M)]
    cost[0][0] = dance(ts_a[0], ts_b[0])
    for i in range(1, M):
        cost[i][ 0] = cost[i - 1][ 0] + dance(ts_a[i], ts_b[0])

    for j in range(1, N):
        cost[0][ j] = cost[0][ j - 1] + dance(ts_a[0], ts_b[j])
    for i in range(1, M):
        for j in range(max(1, i - mww), min(N, i + mww)):
            choices = phe_protocol.PHEProtocol(phe_protocol.PHEProtocol(cost[i - 1][ j - 1]).phe_min(cost[i][ j - 1])).phe_min(cost[i - 1][j])
            cost[i][j]=choices + dance(ts_a[i], ts_b[j])

    # Return DTW distance given window
    return cost[-1][ -1]
def dance(m,n):
    """
    Calculate the distance between two points
    :param m: the point one
    :param n: the point two
    """
    x = phe_protocol.PHEProtocol(m[0]-n[0]).phe_mul(m[0]-n[0])+phe_protocol.PHEProtocol(m[1]-n[1]).phe_mul(m[1]-n[1])
    return x


