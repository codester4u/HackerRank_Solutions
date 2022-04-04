#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    res=[]
    for j in range(len(freqs)):
        for i in range(freqs[j]):
            res.append(values[j])
    res.sort()
    def median(L):
        if len(L)%2!=0: return L[len(L)//2]
        return (L[len(L)//2-1]+L[len(L)//2])//2
    if len(res)%2!=0:
        L,X,U=res[:len(res)//2],res[len(res)//2],res[len(res)//2+1:]
        #print(L,X,U)
        print(float(median(U)-median(L)))
    else:
        L,X,U=res[:len(res)//2],res,res[len(res)//2:]
        #print(L,X,U)
        print(float(median(U)-median(L)))
    return 

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
