#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 05
# Problem 1
# 204111 Sec 001

import math

def intersects(x1, y1, r1, x2, y2, r2, epsilon=10 ** -6):
    distance = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5      # to find the distance between the centers of two circle
    if abs(distance - abs(r1 - r2)) < epsilon or abs(distance - (r1 + r2)) < epsilon:       # touch case
        return 0
    elif distance < r1 + r2 and distance > abs(r1 - r2):         # intersect case
        return 1
    else:           # not intersect case
        return -1

def main():
    # receive input from user
    x1 = float(input())
    y1 = float(input())
    r1 = float(input())
    x2 = float(input())
    y2 = float(input())
    r2 = float(input())
    # print result from function
    print(intersects(x1, y1, r1, x2, y2, r2))

if __name__ == '__main__':
    main()



