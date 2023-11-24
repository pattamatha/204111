#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 03
# Problem 5
# 204111 Sec 001

def main():
    # รับตัวเลขจาก user
    number = int(input('Input number: ')) 
    k = int(input('Input digit: '))
    value = int(input('Input digit: '))
    # พิมพ์ตัวเลขหลังจากการเปลี่ยนค่าหลักที่กำหนด
    print(set_kth_digit(number, k, value))

import math

def kth_digit(number, k):
    kth_digit = (abs(number) % (10 ** (k + 1))) // (10 ** k)
    return kth_digit

def set_kth_digit(number, k, value):
    kth_digits = kth_digit(number, k)
    set_kth_digit = (number - (kth_digits * (10 ** k))) + (value * (10 ** k))
    return set_kth_digit

if __name__ == '__main__':
    main()
