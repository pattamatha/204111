#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Midterm 1/64
# Problem 2
# 204111 Sec 001


def main():
    n = 0
    click = 0
    num = []

    while n != -1:
        n = int(input())
        num += [n]
        if len(num) > 0:
            click = len(num) - 1
        else:
            click = 0

    print("Number of clicks:",click)
    
if __name__ == '__main__':
    main()
