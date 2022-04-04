#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr.sort()
    def median(L):
        if len(L)%2!=0: return L[len(L)//2]
        return (L[len(L)//2-1]+L[len(L)//2])//2
    if len(arr)%2!=0:
        L,X,U=arr[:len(arr)//2],arr[len(arr)//2],arr[len(arr)//2+1:]
        #print(L,X,U)
        return [median(L),X,median(U)]
    else:
        L,X,U=arr[:len(arr)//2],arr,arr[len(arr)//2:]
        #print(L,X,U)
    return [median(L),median(X),median(U)]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()