#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinimumDifference' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY a
#  2. STRING_ARRAY b
#
from collections import Counter

def getMinimumDifference(a, b):
    # Write your code here
    output = []
    
    size = len(a)
    for i in range(size):
        print(a[i])
        print(b[i])
        if len(a[i]) != len(b[i]):
            output.append(-1)
        else:
            count = Counter(a[i]) - Counter(b[i])                  
            output.append(sum(count.values()))
        
    return output
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = input()
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = input()
        b.append(b_item)

    result = getMinimumDifference(a, b)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
