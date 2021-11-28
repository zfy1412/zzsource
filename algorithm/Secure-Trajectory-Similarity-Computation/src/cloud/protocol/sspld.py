#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhan Shi
Time  : 2021/5/12 14:05
"""
import random
import time

import pandas as pd
import phe

import keypair
from src.cloud.protocol import phe_protocol


def phe_sspld(pk, p0, p1, p2):
    """
    Secure Squared Point Line-segment Distance
    :param pk: PHE public key
    :param p0: point 0
    :param p1: point 1
    :param p2: point 2
    :return: distance between point p0 and line-segment p1p2
    """
    a_squared = phe_protocol.PHEProtocol(p0[0] - p1[0]).phe_pow() + phe_protocol.PHEProtocol(p0[1] - p1[1]).phe_pow()
    b_squared = phe_protocol.PHEProtocol(p0[0] - p2[0]).phe_pow() + phe_protocol.PHEProtocol(p0[1] - p1[1]).phe_pow()
    c_squared = phe_protocol.PHEProtocol(p1[0] - p2[0]).phe_pow() + phe_protocol.PHEProtocol(p0[1] - p1[1]).phe_pow()

    left = (phe_protocol.PHEProtocol(p0[0]).phe_mul(p1[1]) +
            phe_protocol.PHEProtocol(p1[0]).phe_mul(p2[1]) +
            phe_protocol.PHEProtocol(p2[0]).phe_mul(p0[1]))
    right = (phe_protocol.PHEProtocol(p1[0]).phe_mul(p0[1]) +
             phe_protocol.PHEProtocol(p2[0]).phe_mul(p1[1]) +
             phe_protocol.PHEProtocol(p0[0]).phe_mul(p2[1]))
    area_triangle_squared = phe_protocol.PHEProtocol(left - right).phe_pow()
    h_squared = phe_protocol.PHEProtocol(area_triangle_squared).phe_truediv(c_squared)

    r1 = random.SystemRandom().randrange(1, pk.n & 0xffffff)
    r2 = random.SystemRandom().randrange(1, pk.n & 0xffffff)
    alpha = (b_squared - a_squared - c_squared) * r1
    beta = (a_squared - b_squared - c_squared) * r2
    theta = phe_third_sspld(alpha, beta, pk)

    delta = [a_squared, b_squared, h_squared]
    distance_squared_1 = phe_protocol.PHEProtocol(delta[0]).phe_mul(theta[0])
    distance_squared_2 = phe_protocol.PHEProtocol(delta[1]).phe_mul(theta[1])
    distance_squared_3 = phe_protocol.PHEProtocol(delta[2]).phe_mul(theta[2])

    return distance_squared_1 + distance_squared_2 + distance_squared_3


def phe_third_sspld(alpha, beta, pk):
    """
    Secure Squared Point Line-segment Distance
    :param alpha: param 1
    :param beta: param 2
    :param pk: PHE public key
    :return: an encrypted sequence theta
    """
    private_key = pd.read_pickle(keypair.PRIVATE_KEY_PATH)
    sk = phe.PaillierPrivateKey(p=int(private_key.loc['p'][0]),
                                public_key=pk, q=int(private_key.loc['q'][0]))

    if sk.decrypt(alpha) >= 0:
        theta = [pk.encrypt(1), pk.encrypt(0), pk.encrypt(0)]
    elif sk.decrypt(beta) >= 0:
        theta = [pk.encrypt(0), pk.encrypt(1), pk.encrypt(0)]
    else:
        theta = [pk.encrypt(0), pk.encrypt(0), pk.encrypt(1)]

    return theta


if __name__ == '__main__':
    pk = phe.PaillierPublicKey(n=int(pd.read_pickle(keypair.PUBLIC_KEY_PATH).loc['n'][0]))

    private_key = pd.read_pickle(keypair.PRIVATE_KEY_PATH)
    sk = phe.PaillierPrivateKey(p=int(private_key.loc['p'][0]),
                                public_key=pk, q=int(private_key.loc['q'][0]))

    p0 = [pk.encrypt(1), pk.encrypt(1)]
    p1 = [pk.encrypt(2), pk.encrypt(2)]
    p2 = [pk.encrypt(3), pk.encrypt(3)]

    s = time.time()
    for _ in range(10):
        a = phe_sspld(pk, p0, p1, p2)
    print(time.time() - s)
    print(sk.decrypt(a))
