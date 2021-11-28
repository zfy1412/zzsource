#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhan Shi
Time  : 2021/5/7 11:23
"""
import random

import pandas as pd
import phe

from keypair import PUBLIC_KEY_PATH, PRIVATE_KEY_PATH


class PHEProtocol(object):
    """
    PHEProtocol
    """

    def __init__(self, c):
        """
        PHEProtocol Class
        :param c: EncryptedNumber
        """
        self.c = c

    # def phe_mul(self, other):
    #     """
    #     PHE mul protocol
    #     :param other: other EncryptedNumber
    #     return self * other
    #     """
    #     r1 = self._generate_random()
    #     r2 = self._generate_random()
    #
    #     h1 = self.c * r1
    #     h2 = other * r2
    #
    #     return PHEThirdProtocol().phe_third_mul(h1, h2) / (r1 * r2)

    def phe_mul(self, other):
        """
        PHE mul protocol
        :param other: other EncryptedNumber
        :return: self * other
        """
        r1 = self._generate_random()
        r2 = self._generate_random()

        h1 = self.c + self.c.public_key.encrypt(r1)
        h2 = other + self.c.public_key.encrypt(r2)

        return (PHEThirdProtocol().phe_third_mul(h1, h2) -
                self.c * r2 - other * r1 - self.c.public_key.encrypt(r1 * r2))

    def phe_truediv(self, other):
        """
        PHE div protocol
        :param other: other EncryptedNumber
        :return: self / other
        """
        r1 = self._generate_random()
        r2 = self._generate_random()

        h1 = self.c * r1 + other * r1 * r2
        h2 = other * r1

        return PHEThirdProtocol().phe_third_truediv(h1, h2) - self.c.public_key.encrypt(r2)

    # def phe_pow(self):
    #     """
    #     PHE pow 2 protocol
    #     return self ** 2
    #     """
    #     r = self._generate_random()
    #
    #     h = self.c * r
    #
    #     return PHEThirdProtocol().phe_third_pow(h) / (r ** 2)

    def phe_pow(self):
        """
        PHE pow 2 protocol
        :rtype: object
        :return: number pow 2
        """
        r1 = self._generate_random()
        r2 = self._generate_random()

        h1 = self.c + self.c.public_key.encrypt(r1)
        h2 = self.c + self.c.public_key.encrypt(r2)

        return (PHEThirdProtocol().phe_third_mul(h1, h2) -
                self.c * (r2 - r1) - self.c.public_key.encrypt(r1 * r2))

    def phe_min(self, other):
        """
        PHE min protocol
        :param other: other EncryptedNumber
        :return: min number between the two number
        """
        r1 = self._generate_random()
        r2 = self._generate_random()
        r3 = self._generate_random()

        if random.random() > 0.5:
            h = (self.c - other) * r1
            h1 = self.c + self.c.public_key.encrypt(r2)
            h2 = other + self.c.public_key.encrypt(r3)
        else:
            h = (other - self.c) * r1
            h1 = other + self.c.public_key.encrypt(r2)
            h2 = self.c + self.c.public_key.encrypt(r3)

        alpha, beta = PHEThirdProtocol().phe_third_min(h, h1, h2)

        return self.c + other - beta + alpha * r3 + (self.c.public_key.encrypt(1) - alpha) * r2

    def _generate_random(self):
        """
        Generate big random number
        :return: big random number
        """
        return random.SystemRandom().randrange(1, self.c.public_key.n & 0xffffff)


class PHEThirdProtocol(object):
    """
    PHEThirdProtocol
    """

    def __init__(self):
        """
        PHEThirdProtocol Class
        """
        self.pk = phe.PaillierPublicKey(n=int(pd.read_pickle(PUBLIC_KEY_PATH).loc['n'][0]))

        private_key = pd.read_pickle(PRIVATE_KEY_PATH)
        self.sk = phe.PaillierPrivateKey(p=int(private_key.loc['p'][0]),
                                         public_key=self.pk, q=int(private_key.loc['q'][0]))

    def phe_third_mul(self, h1, h2):
        """
        PHE mul protocol third part
        :param h1: param 1
        :param h2: param 2
        :return: EncryptedNumber mul param
        """
        return h1.public_key.encrypt(self.sk.decrypt(h1) * self.sk.decrypt(h2))

    def phe_third_truediv(self, h1, h2):
        """
        PHE div protocol third part
        :param h1: param 1
        :param h2: param 2
        :return: EncryptedNumber div param
        """
        return h1.public_key.encrypt(self.sk.decrypt(h1) / self.sk.decrypt(h2) if self.sk.decrypt(h2) != 0 else 0)

    def phe_third_pow(self, h):
        """
        PHE pow 2 protocol third part
        :param h: param 1
        :return: EncryptedNumber pow 2 param
        """
        return h.public_key.encrypt(self.sk.decrypt(h) ** 2)

    def phe_third_max(self, h, h1, h2):
        """
        PHE max protocol third part
        :param h: difference between two numbers
        :param h1: the first number or the second number
        :param h2: the first number or the second number
        :return: alpha, beta
        """
        alpha = 1 if self.sk.decrypt(h) > 0 else 0

        return h.public_key.encrypt(alpha), h2 if alpha == 1 else h1

    def phe_third_min(self, h, h1, h2):
        """
        PHE min protocol third part
        :param h: difference between two numbers
        :param h1: the first number or the second number
        :param h2: the first number or the second number
        :return: alpha, beta
        """
        alpha = 1 if self.sk.decrypt(h) < 0 else 0

        return h.public_key.encrypt(alpha), h2 if alpha == 1 else h1

    def phe_third_le(self, h):
        """
        PHE compare le protocol third part
        :param h: param
        :return: whether <=
        """
        return self.sk.decrypt(h) <= 0
