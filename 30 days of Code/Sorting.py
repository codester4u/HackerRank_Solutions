#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    count=0
    for i in range(n-1):
        for i in range(n-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                count+=1
    print("Array is sorted in",count,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
