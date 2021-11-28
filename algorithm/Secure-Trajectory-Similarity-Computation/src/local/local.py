#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhan Shi
Time  : 2021/5/7 12:10
"""
import tqdm
from colorama import Fore

from src.local.grid import generate
from src.util.timer import timer


def data_owner(cnt, path, dmax):
    """
    Data Owner
    :param dmax: width of the survey grid signature
    :param path: trajectory dataset name
    :param n: the number of iteration
    :return: some params
    """
    # p_bar = tqdm.tqdm(range(1, int(n) + 1))
    # for i in p_bar:
    length = len(cnt)
    for i in range(0, length):
        file_name = f"{path}_{str(cnt[i]).zfill(5)}.csv"
        # p_bar.set_description(f"{Fore.YELLOW}Generate Grid Signature [{dmax}] [{file_name}]")
        generate.generate_grid(file_name, path, int(dmax))

    return "DOR", path, cnt, dmax


def user(name, dmax):
    """
    User
    :param dmax: width of the survey grid signature
    :param name: name of query trajectory
    :return: some params
    """
    # p_bar = tqdm.tqdm(range(1))
    # for _ in p_bar:
        # p_bar.set_description(f"{Fore.YELLOW}Generate Grid Signature [{dmax}] [{name}_query.csv]")
    for _ in range(1):
        generate.generate_grid(f"{name}_query.csv", "query", int(dmax))

    return "USR", name, '1', dmax
