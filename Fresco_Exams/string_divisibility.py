#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSmallestDivisor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

def findSmallestDivisor(s, t):
    # Write your code here
    slen = len(s)
    tlen = len(t)
    tcopy = t
    
    while(slen>tlen):
        t = tcopy + t
        tlen = len(t)
        
    if(s==t):
        i = (s+s)[1:-1].find(s)
        if i == -1:
            rt = s
        else:
            rt = s[:i+1]
            
        return(len(rt))
    else:
        return(-1)    
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    result = findSmallestDivisor(s, t)

    fptr.write(str(result) + '\n')

    fptr.close()
