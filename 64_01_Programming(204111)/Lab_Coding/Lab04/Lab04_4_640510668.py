#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 04
# Problem 4
# 204111 Sec 001

def round_to_int(x):
    # WRITE YOUR CODE HERE
    if x >= 0:                      # x is positive number
        if x - int(x) >= 0.5:       
            return int(x) + 1
        else:
            return int(x)
    else:                           # x is negative number
        if x - int(x) <= (-0.5):
            return int(x) - 1
        else:
            return int(x)

def main():
    # receive input from user
    x = float(input())
    # print result from function
    print(round_to_int(x))

if __name__ == '__main__':
    main()
