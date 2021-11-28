#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhao Fanyou
Time  : 2021/11/9 00:42
"""
import sys
from time import *
from src.cloud import cloud
from src.local import local
import keypair


def local_processing():
    """
    Local processing
    """
    local.data_owner(sys.argv[2], name)
    local.user(name)


def cloud_processing():
    """
    Cloud processing
    """
    cloud.cloud(name, sys.argv[2],threshold)


if __name__ == '__main__':
    # the first param determines Key length (256，512，1024...)
    # the second param determines the sequence of trajectories in the trajectory dataset(1,2,3,...100)
    # the third param determines the name of trajectory dataset(normal, uniform, SHH-Taxi,T-drive)
    # the third param determines the distance threshold dataset(10，50，100，200)     DTW没有，DTW只有三个代码,其他都有
    #DTW相似度越小越相似，lcss越大越相似
    name = sys.argv[3]
    threshold = ((int(sys.argv[4])*100000*100000)/30.9)/3600
    time1 = time()
    keypair.generate_keypair(int(sys.argv[1]))
    local_processing()
    cloud_processing()
    time2 = time()
    print(time2 - time1)

