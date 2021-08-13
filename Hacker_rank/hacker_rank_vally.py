#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    ans =0
    vally =0
    for i in path:
        if i == 'D':
            vally-=1
        if i=='U':
            vally+=1
        print(vally)
        if vally == 0 and i == 'U':
            ans+=1
    return ans
if __name__ == '__main__':
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)