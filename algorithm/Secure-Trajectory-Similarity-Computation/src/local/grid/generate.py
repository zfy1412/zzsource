#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhan Shi
Time  : 2021/5/12 13:51
"""
import pandas as pd
import phe

import keypair
from src.local.grid import result as res, signature as sig


def generate_grid(file, path, survey_grid_width):
    """
    Generate grid signature
    :param path: trajectory dataset
    :param survey_grid_width: survey grid width
    :param file: trajectory file name
    :return: the file of grid signature
    """
    name = f"resource/{path}/{file}"
    p = pd.read_csv(name, header=None, usecols=[0, 1], dtype=float, encoding='utf-8', engine='python')
    points = ((p.values * 100000 / (survey_grid_width // 10)).round() * (survey_grid_width // 10) + 18000000).tolist()

    result = res.Result()
    public_key = phe.PaillierPublicKey(n=int(pd.read_pickle(keypair.PUBLIC_KEY_PATH).loc['n'][0]))
    grid = None
    for i in range(len(points)):
        try:
            if points[i] == points[i - 1] and i > 1:
                result.add(grid)
                continue
            else:
                grid = sig.Grid(survey_grid_width, public_key, p1=points[i], p2=points[i + 1])
        except IndexError:
            grid = sig.Grid(survey_grid_width, public_key, p1=points[i])

        result.add(grid)

    sgw = str(survey_grid_width)
    file_name = f"encryption/{path}/{sgw}/{file.strip('.csv')}_{sgw}.pkl"
    result.unique_dataframe(public_key, points).to_pickle(file_name)

    return "Generate Grid Signature [%s]" % file
