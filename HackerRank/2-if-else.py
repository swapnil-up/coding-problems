#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (n%2==1):
        print(f"Weird")
    elif (2<=n<=5):
        print (f"Not Weird")
    elif (6<=n<=20):
        print(f"Weird")
    elif (n>20 and n%2==0):
        print (f"Not Weird")
