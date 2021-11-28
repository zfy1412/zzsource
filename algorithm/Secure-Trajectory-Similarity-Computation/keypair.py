#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhan Shi
Time  : 2021/5/6 14:53
"""
import sys

import pandas as pd
import phe
from colorama import Fore, Style

# the files of the key pair
PUBLIC_KEY_PATH = "encryption/keypair/public.key"
PRIVATE_KEY_PATH = "encryption/keypair/private.key"


def generate_keypair(length):
    """
    Generate PHE keypair with 'length' key-lengths
    :param length: key-lengths
    """
    # generate PHE keypair with 'length' key-lengths using 'phe' (python package)
    (public_key, private_key) = phe.generate_paillier_keypair(n_length=length)
    # vary the keypair to data style of pandas.DataFrame (python package)
    pd.DataFrame(data=[public_key.n], index=['n']).to_pickle(PUBLIC_KEY_PATH)
    pd.DataFrame(data=[private_key.p, private_key.q], index=['p', 'q']).to_pickle(PRIVATE_KEY_PATH)
    # print the message of generating PHE keypair
    # print(f"{Fore.RED}{Style.BRIGHT}The keypair is successfully generated with [{length}]-lengths.\n"
    #       f"{Fore.YELLOW}The file of the public key is [{PUBLIC_KEY_PATH}].\n"
    #       f"{Fore.BLUE}The file of the private key is [{PRIVATE_KEY_PATH}].{Style.RESET_ALL}")


if __name__ == '__main__':
    # the first param is length of the PHE keypair (256, 512, 1024, 2048,...)
    generate_keypair(length=int(sys.argv[1]))
