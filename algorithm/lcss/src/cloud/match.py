#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhao Fanyou
Time  : 2021/11/9 00:42
"""
import phe
import keypair
import pandas as pd
from src.cloud.protocol import phe_protocol


def point_equal(m,n,threshold):
    """
    Judge two-point algorithm matching
    :param m: the point one
    :param n: the point two
    :param threshold: the distance threshold dataset
    """
    pk = phe.PaillierPublicKey(n=int(pd.read_pickle(keypair.PUBLIC_KEY_PATH).loc['n'][0]))
    enthreshold=pk.encrypt(threshold*1.0)
    x = phe_protocol.PHEProtocol(m[0]-n[0]).phe_mul(m[0]-n[0])+phe_protocol.PHEProtocol(m[1]-n[1]).phe_mul(m[1]-n[1])
    y = enthreshold
    if phe_protocol.PHEProtocol(x).pin_boolmore(y):
        return False
    else:
        return True


def lcss(a,b,threshold):
    """
    LCSS algorithm
    :param a: the point set one
    :param b: the point set two
    :param threshold: the distance threshold dataset
    """
    lena = len(a)
    lenb = len(b)
    L = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    for i in range(lena+1):
      for j in range(lenb+1):
        if i==0 or j==0:
          L[i][j] = 0
        elif point_equal(a[i-1],b[j-1],threshold):
          L[i][j] = L[i-1][j-1] + 1
        else:
          L[i][j] = max(L[i-1][j],L[i][j-1])
    return L[lena][lenb]
