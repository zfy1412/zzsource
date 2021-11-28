#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhao Fanyou
Time  : 2021/11/9 20:42
"""
import phe
import keypair
import pandas as pd

from src.cloud import match

def cloud(name, n):
    """
    Cloud
    :param n: the sequence of trajectories in the trajectory dataset
    :param name: the name of trajectory dataset
    """
    query_name = f"{name}_query.pkl"
    query = pd.read_pickle(f"encryption/query/{query_name}")
    query_point = [p for p in query.loc['p'] if p is not None]
    file_name = f"{name}_{n.zfill(5)}.pkl"
    point = pd.read_pickle(f"encryption/{name}/{file_name}")
    pointlist = [p for p in point.loc['p'] if p is not None]
    private_key = pd.read_pickle(keypair.PRIVATE_KEY_PATH)
    pk = phe.PaillierPublicKey(n=int(pd.read_pickle(keypair.PUBLIC_KEY_PATH).loc['n'][0]))
    sk = phe.PaillierPrivateKey(p=int(private_key.loc['p'][0]),
                                public_key=pk, q=int(private_key.loc['q'][0]))
    print(sk.decrypt(match.dtw_distance(pointlist, query_point))/10000000000)


