#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    cp,cm,cz=0,0,0
    for i in arr:
        if i>0:
            cp+=1
        elif i<0:
            cm+=1
        else:
            cz+=1
    print("%.6f" % float(cp/n))
    print("%.6f" % float(cm/n))
    print("%.6f" % float(cz/n))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
