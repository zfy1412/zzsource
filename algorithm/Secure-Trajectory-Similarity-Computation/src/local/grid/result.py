#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhan Shi
Time  : 2021/5/12 13:50
"""
import pandas as pd


class Result(object):
    """
    Class Result
    """

    def __init__(self):
        """
        Result initialize
        """
        self.tg = list()
        self.sg = list()

    def add(self, other):
        """
        Add grid to result
        :param other: other grid signature
        """
        self.tg.extend(other.tg)
        self.sg.append(other.sg)

    def unique_dataframe(self, pk, points):
        """
        Encrypt the data about trajectory and output the data
        :param pk: public key
        :param points: coordinate of trajectory
        :return: dealed encrypted data about trajectory
        """
        # filter the same TGS and encrypt TGS
        self.tg = list(set(pk.encrypt(v) for v in self.tg))

        # encrypt SGS
        survey_grid = list()
        for grids in self.sg:
            survey_grid.append(list(pk.encrypt(v) for v in grids))
        # encrypt coordinate of trajectory
        points = [[pk.encrypt(point[0]), pk.encrypt(point[1])] for point in points]
        # generate the vector of the max trajectory length
        length = [pk.encrypt(1) for _ in points]

        return pd.DataFrame(data=[self.tg, survey_grid, points, length], index=['tg', 'sg', 'p', 'l'])
