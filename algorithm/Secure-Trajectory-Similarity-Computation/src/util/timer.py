#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhan Shi
Time  : 2021/5/7 10:34
"""
import logging as log
import time


def timer(function):
    """
    Calculate the function runtime
    :param function: running function
    :return: function running time
    """

    def wrapper(*args, **kwargs):
        """
        Timer wrapper
        :param args:
        :param kwargs:
        :return: function result
        """
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        cost_time = (end_time - start_time)
        # create log file
        space = ' ' * 5
        file_handle_cost_time = log.FileHandler("log/time.log", 'a', encoding='utf-8')
        file_handle_cost_time.setFormatter(log.Formatter(fmt=f"%(asctime)s{space}%(message)s"))
        logger_cost_time = log.Logger('', level=log.INFO)
        logger_cost_time.addHandler(file_handle_cost_time)
        # content of log file
        dataset_name = ("NOR" if result[1] == "normal" else
                        "UNI" if result[1] == "uniform" else
                        "SHH" if result[1] == "SHH-Taxi" else
                        "TDR" if result[1] == "T-drive" else '')
        # logger_cost_time.info(f"{result[0]}{space}{dataset_name}{space}"
        #                       f"{result[2].rjust(3, ' ')}{space}{result[3].rjust(3, ' ')}{space}{cost_time}")

        return result

    return wrapper
