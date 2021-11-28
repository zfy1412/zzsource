#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhao Fanyou
Time  : 2021/11/9 00:42
"""
import tqdm
from colorama import Fore
import pandas as pd
import keypair
import phe


def data_owner(n, name):
    """
    Data Owner
    :param name: the name of trajectory dataset
    :param n: the sequence of trajectories in the trajectory dataset
    """

    pk = phe.PaillierPublicKey(n=int(pd.read_pickle(keypair.PUBLIC_KEY_PATH).loc['n'][0]))
    file_name = f"resource/{name}/{name}_{str(n).zfill(5)}.csv"
    p = pd.read_csv(file_name, header=None, usecols=[0, 1], dtype=float, encoding='utf-8', engine='python')
    points = (p.values*100000).tolist()
    points = [[pk.encrypt(point[0]), pk.encrypt(point[1])] for point in points]
    to=f"encryption/{name}/{name}_{str(n).zfill(5)}.pkl"
    pd.DataFrame(data=[points], index=['p']).to_pickle(to)



def user(name):
    """
    User
    :param name: name of query trajectory
    """
    pk = phe.PaillierPublicKey(n=int(pd.read_pickle(keypair.PUBLIC_KEY_PATH).loc['n'][0]))
    for _ in range(1):
        file_name = f"resource/query/{name}_query.csv"
        # p_bar.set_description(f"{Fore.YELLOW}Generate Grid Signature [{dmax}] [{file_name}]")
        p = pd.read_csv(file_name, header=None, usecols=[0, 1], dtype=float, encoding='utf-8', engine='python')
        points = (p.values*100000).tolist()
        points = [[pk.encrypt(point[0]), pk.encrypt(point[1])] for point in points]
        to = f"encryption/query/{name}_query.pkl"
        pd.DataFrame(data=[points], index=['p']).to_pickle(to)

