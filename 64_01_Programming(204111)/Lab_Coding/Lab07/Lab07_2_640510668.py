#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 07
# Problem 2
# 204111 Sec 001

import math

def digit_count(x, base=10):
    count = 1   # ใช้นับจำนวนครั้งที่หารได้ (เริ่มที่ count = 1 เพราะนับตัวสุดท้ายที่ไม่ถูกหาร)
    while abs(x) // base > 0:
        count += 1
        x = abs(x) // base
    return count
    # การแปลงเลขฐาน 10 ให้เป็นเลขฐาน base(input)
    # สามารถทำได้โดยการนำ x(input) มาหารด้วย base(input) ไปเรื่อยๆ จนกว่าได้ผลหารเท่ากับ 0
    # ขณะที่หาร ให้นับจำนวนครั้งที่หารได้ จะได้จำนวนตัวเลขที่แปลงเป็น base นั้นๆ

def test_digit_count(x, base):
    test = digit_count(x, base=10)
    # assert เงื่อนไขที่จะไม่เกิดข้อผิดพลาด
    assert(test)
    # เช่น x = 123, base = 2
    # output = 7

def main():
    x = int(input("number: "))
    base = input("base: ")
    if base == "":
        print(digit_count(x))
    else:
        base = int(base)
        print(digit_count(x,base))


if __name__ == '__main__':
    main()
