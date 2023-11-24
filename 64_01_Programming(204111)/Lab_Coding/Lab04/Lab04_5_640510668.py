#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 04
# Problem 5
# 204111 Sec 001

import math

def nearest_odd(x):
    # WRITE YOUR CODE HERE
    if x >= 0:                              # x is positive number
        if int(x) % 2 == 0:                 # if x is even number
            if x - int(x) >= 0:             # if x is float
                return int(x) + 1
            if x - int(x) == 0:             # if x is int
                return int(x) - 1
        else:                               # if x is odd number
            if x - int(x) > 0:              # if x is float
                return int(x)
            if x - int(x) == 0:             # if x is int
                return int(x)
    else:                                   # x is negative number
        if int(x) % 2 == 0:                 # if x is even number
            if abs(x) - abs(int(x)) > 0:    # if x is float
                return int(x) - 1
            if abs(x) - abs(int(x)) == 0:   # if x is int
                return int(x) + 1
        else:                               # if x is odd number
            if abs(x) - abs(int(x)) > 0:    # if x is float
                return int(x)
            if abs(x) - abs(int(x)) == 0:   # if x is int
                return int(x)

def main():
    # receive input from user
    x = float(input())
    # print result from function
    print(nearest_odd(x))

if __name__ == '__main__':
    main()
