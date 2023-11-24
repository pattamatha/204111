#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 03
# Problem 4
# 204111 Sec 001

def main():
    # รับตัวเลขจาก user
    number = int(input('Input number: ')) 
    k = int(input('Input digit: '))
    # พิมพ์ตัวเลขตำแหน่งที่ k ของข้อมูลเข้า
    print(kth_digit(number, k))

import math

def kth_digit(number, k):
    kth_digit = (abs(number) % (10 ** (k + 1))) // (10 ** k)
    return kth_digit


if __name__ == '__main__':
    main()
