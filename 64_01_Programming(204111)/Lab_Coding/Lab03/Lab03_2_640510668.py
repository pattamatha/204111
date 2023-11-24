#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 03
# Problem 2
# 204111 Sec 001

def reverse_digits(x):
    unit_digit = x // 1000
    ten_digit = ((x // 100) % 10) * 10
    hundred_digit = ((x // 10) % 10) * 100
    thousands_digit = (x % 10) * 1000
    return unit_digit + ten_digit + hundred_digit + thousands_digit

def main():
    # รับตัวเลขจาก user
    x = int(input())
    # พิมพ์ตัวเลขกลับด้าน
    print(reverse_digits(x))

if __name__ == '__main__':
    main()
