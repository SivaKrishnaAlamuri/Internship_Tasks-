# problem6

import os

def pangrams(s):
    s = s.lower()
    
    unique_letters = {char for char in s if 'a' <= char <= 'z'}
    
    if len(unique_letters) == 26:
        return 'pangram'
    else:
        return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
