# python 14
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s) % 2 != 0:
        return -1
    
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
    count = 0
    s2_list = list(s2)
    
    for char in s1:
        if char in s2_list:
            s2_list.remove(char)  
        else:
            count += 1  
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

