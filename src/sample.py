#!/usr/bin/env python
# coding: utf-8


from __future__ import print_function

from ChaPAS import ChaPAS
from config import CHAPAS_PATH

import argparse

def main(mode, text):
    chapas = ChaPAS(CHAPAS_PATH)
    result = chapas.parse(text, mode)
    
    for items in result:
        for item in items:
            print(item)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", "-m", type=str, help='parser mode')
    parser.add_argument("--text", "-t", type=str, default="")

    args = parser.parse_args()
    main(args.mode, args.text)
