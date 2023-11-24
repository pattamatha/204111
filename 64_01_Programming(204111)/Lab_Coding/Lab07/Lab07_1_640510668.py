#!#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 07
# Problem 1
# 204111 Sec 001

import math
def main():
    x  = int(input())
    y  = int(input())
    print(sum_prime_in_range(x, y))

# สามารถใช้ is_prime() เพื่อตรวจสอบว่าตัวเลขนั้นๆ 
# เป็น prime number หรือไม่
def is_prime(x):
    div = 2
    while div <= math.sqrt(x):
        if x % div == 0:
            return False
        else:
            if div == 2:
                div = 3
            else:
                div += 1
    return True

#รวมตัวเลขเฉพาะที่เป็นเลข prime number จาก x ถึง y
def sum_prime_in_range(x, y):
    result = 0               # เพื่อเก็บผลรวมทั้งหมด
    while x <= y:           
        prime = is_prime(x)  # เพื่อตรวจสอบว่า x เป็นค่า prime หรือไม่
        if prime == True:
            result += x      # ถ้า x เป็น prime ให้บวกค่า x ลงไปใน result 
        x += 1               # อัพเดตค่า x
    return result


if __name__ == '__main__':
    main()
