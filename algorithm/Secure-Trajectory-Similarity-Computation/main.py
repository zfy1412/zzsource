#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhan Shi
Time  : 2021/5/7 10:30
"""
import sys
import keypair
from src.cloud import cloud
from src.local import local
from time import *



def local_processing():
    """
    Local processing
    """
    for name in dataset:
        for threshold in distance_max:
            local.data_owner(cnt, name, threshold)
            local.user(name, threshold)


def cloud_processing():
    """
    Cloud processing
    """
    for name in dataset:
        for threshold in distance_max:
            cloud.cloud(cnt, name, threshold)


if __name__ == '__main__':
    # the first param determines Key length (256，512，1024...)
    # the second param determines the distance threshold dataset(10，50，100，200)
    # the third param determines the name of trajectory dataset(normal, uniform, SHH-Taxi,T-drive)
    # the fourth param determines the sequence of trajectories in the trajectory dataset(1,2,3,...100)
    namez = sys.argv[3]
    dmax = sys.argv[2]
    dataset = [namez]  # normal, uniform, SHH-Taxi,T-drive
    distance_max = [dmax]
    n = 1

    cnt=[]
    cnt.append(int(sys.argv[4]))
    time1 = time()
    keypair.generate_keypair(int(sys.argv[1]))
    local_processing()
    cloud_processing()
    time2 = time()
    print(time2 - time1)