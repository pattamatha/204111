#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 07
# Problem 5
# 204111 Sec 001

def main():
    num = int(input("num: "))
    pos = int(input("pos: "))
    result = rotate(num, pos)
    print(type(result))
    print(result)

import math

def rotate(num, pos):
    result = 0                      # เพื่อเก็บผลลัพธ์
    num0 = int(math.log10(num))     # คำนวณหาจำนวนตัวเลขของ num
    num1 = 0     # เพื่อใช้เก็บค่าที่คำนวณได้ในส่วนแรก
    num2 = 0     # เพื่อใช้เก็บค่าที่คำนวณได้ในส่วนที่สอง
    if num == 0:
        result = num 
    if pos >= 0:
        for i in range(pos):
            num1 = (num % 10) * (10 ** num0)
            num2 =  num // 10
            result = num1 + num2
            num = result
            pos -= 1
    else: # pos < 0:
        for i in range(abs(pos)):
            num1 = num // (10 ** num0)
            num2 = (num % (10 ** num0)) * 10
            result = num1 + num2
            num = result
            pos += 1
    return result


if __name__ == '__main__':
    main()
