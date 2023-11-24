#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 04
# Problem 1
# 204111 Sec 001

import math

def love6(first, second):
    if (first == 6) or (second == 6):      # each of them is 6
        return True
    elif first + second == 6:              # sum of two is 6
        return True
    elif first - second == 6:              # diff of two is 6
        return True
    elif abs(first - second) == 6:         # diff of two is 6
        return True
    else:
        return False
        
def main():
    # receive input from user
    first = int(input())
    second = int(input())
    # print result from function
    print(love6(first,second))

if __name__ == '__main__':
    main()
