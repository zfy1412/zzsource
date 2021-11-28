#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhao Fanyou
Time  : 2021/11/9 00:42
"""
import pandas as pd

from src.cloud import match

def cloud(name, n, threshold):
    """
    Cloud
    :param n: the sequence of trajectories in the trajectory dataset
    :param name: the name of trajectory dataset
    :param threshold: the distance threshold dataset
    """
    query_name = f"{name}_query.pkl"
    query = pd.read_pickle(f"encryption/query/{query_name}")
    query_point = [p for p in query.loc['p'] if p is not None]
    file_name = f"{name}_{str(n).zfill(5)}.pkl"
    point = pd.read_pickle(f"encryption/{name}/{file_name}")
    pointlist = [p for p in point.loc['p'] if p is not None]
    print(match.lcss(pointlist, query_point,threshold))


