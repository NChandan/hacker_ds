#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
import itertools as it

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    output = [0] * n
    out = defaultdict(int)
    # try:
    #     for a, b, k in queries:
    #         for i in range(a - 1, b):
    #             output[i] += k
    #             out[i] += k
    #     # print(output, max(out.values())
    # except Exception as err:
    #     import traceback
    #     traceback.print_exc()
    # return max(output)  # , key=output.count)
    q = it.chain.from_iterable([(a, k), (b, -k)] for a, b, k in queries)
    p = it.accumulate(c for _, c in sorted(q, key=lambda x: (x[0], -x[1])))
    print(max(p))
    q = []
    for a, b, k in queries:
        q.append((a, k))
        q.append((b, -k))

    p = it.accumulate(c for _, c in sorted(q, key=lambda x: (x[0], -x[1])))
    print(max(p))
    print("")
# 2497169732

if __name__ == "__main__":
    queries = []
    b = []
    with open("./input.txt") as file:
        b = file.readline().replace("\n", "").split(" ")
        while True:
            line = file.readline()
            if not line:
                break
            queries.append(list(map(int, line.rstrip().split())))
    print(arrayManipulation(int(b[0]), queries))
    print("sad")