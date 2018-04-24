#!/bin/python3

import os
import sys

#
# Complete the aVeryBigSum function below.

# My code is written below
def aVeryBigSum(n, ar):
	""" Return the sum of the elements in the list."""
    sum_ar = 0
    for i in range(n):
        sum_ar += ar[i]
        
    return sum_ar

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(n, ar)

    f.write(str(result) + '\n')

    f.close()