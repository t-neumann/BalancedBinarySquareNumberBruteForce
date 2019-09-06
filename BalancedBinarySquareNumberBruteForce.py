#!/usr/bin/env python

# Efficient permutation of non-redundant binary numbers:
# https://stackoverflow.com/a/37584849

# Date located in: -
from __future__ import print_function
import sys, itertools, math

def getSquare(x):
    root = math.sqrt(x)
    return int(root + 0.5)

def isSquare(x):
    root = math.sqrt(x)
    if int(root + 0.5) ** 2 == x:
        return True
    return False

def binaryShuffle(length=30, ones=15):

    global globalCount

    result = []
    rr = ['0'] * length  ## initialize empty list with
                         ## ZEROS of given length
    for c in itertools.combinations(range(length), ones):
        r = rr[:] ## create a copy of initialized list
        for x in c:
            r[x] = '1' ## Change ZERO to ONE based on different
                       ## combinations of positions
        number = "".join(r)

        if isSquare(int(number)):
            print("SUCCESS: The square root of " + number, end="")
            print(" is " + str(getSquare(int(number))))
            sys.exit(0)

        globalCount += 1

        if globalCount % 10000000 == 0:
            print(str(globalCount) + " possible solutions evaluated.",
            file=sys.stderr)

globalCount = 0

binaryShuffle()

print("No perfect square found of length 30 with 15 zeros and 15 ones")
print("Total " + str(globalCount) + " combinations evaluated.")
