#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 06
# Problem 1
# 204111 Sec 001

import math

def int_power(x, y):
    result = 1
    if y >= 0:
        for i in range(y):
            result = result * x
        return result
    else:
        for i in range(abs(y)):
            result = result * x
        return (1 / result)
        
def main():
    x = float(input())
    y = int(input())
    print("{:.6f}".format(int_power(x,y)))
    
if __name__ == '__main__':
    main()
