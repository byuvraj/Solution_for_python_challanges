#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    n = len(c)
    ans = 0
    i =0
    while i <= n-3:
        if c[i+2] == 0:
            ans+=1
            i+=2
            if i == n - 2 :
                ans+=1
        elif c[i+1] == 0:
            ans+=1
            i+=1
    if ans == 0:
        return ans + 1
    else:
        return ans
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
