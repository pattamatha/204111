#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 05
# Problem 4
# 204111 Sec 001

# 2 cases
# fisrt case => overlap return True
# second case => not overlap return False

def is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2):
    if l1 > l2 + w2 or l2 > l1 + w1:
        return False
    if t1 > t2 + h2 or t2 > t1 + h1:
        return False
    else:
        return True

def main():
    l1 = int(input())
    t1 = int(input())
    w1 = int(input())
    h1 = int(input())
    l2 = int(input())
    t2 = int(input())
    w2 = int(input())
    h2 = int(input())
    print(is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2))


if __name__ == '__main__':
    main()
