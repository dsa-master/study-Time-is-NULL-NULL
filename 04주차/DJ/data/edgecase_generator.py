"""
Author: Hepheir<hepheir@gmail.com>

최악의 경우일 때(E=100, B=16)의 입출력 임의로 생성하는 코드.
"""

import os
import sys
import random


DIRNAME = os.path.dirname(__file__)
FILENAME = os.path.join(DIRNAME, 'edgecase-random-{}.txt').format
TESTER = os.path.join(DIRNAME, 'tester.out')


def binpad(x: int, len: int) -> str:
    return bin(x).lstrip('0b').zfill(len)


# Create directory

if not os.path.exists(DIRNAME):
    os.mkdir(DIRNAME)


# Create random inputs
with open(FILENAME('input'), 'w') as f:
    MAX_B = 16
    MAX_E = 100
    X_CHECK = set()

    f.write(f'{MAX_B} {MAX_E}\n')
    for e in range(MAX_E+1):
        while True:
            X = random.randint(0, (1 << MAX_B) -1)
            if X not in X_CHECK:
                break
        X_CHECK.add(X)
        f.write(binpad(X, MAX_B)+'\n')


# Create output for generated input
os.system(' '.join([TESTER, '<', FILENAME('input'), '>', FILENAME('output')]))


# You can import this module to test your result
sys.stdin = open(FILENAME('input'), 'r')