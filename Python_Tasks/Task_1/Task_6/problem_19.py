# python19

from collections import Counter
import math
import os
import random
import re
import sys

if __name__ == '__main__':
  s = input()
  chars = Counter(s).items()
  for char, n in sorted(chars, key=lambda c: (-c[1], c[0]))[:3]:
    print(char, n)
