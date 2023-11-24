#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 06
# Problem 2
# 204111 Sec 001

def float_to_bin(x):
    x_int = int(x)         # ได้จำนวนเต็ม ไม่มีทศนิยม
    x_float = x - int(x)   # ได้ทศนิยม

    # ใช้คำนวณส่วนที่เป็นจำนวนเต็ม
    result1 = 0     # เอาไว้เก็บจำนวนฐานสอง
    remainder = 0   # เอาไว้เก็บค่า remainder
    n = 0           # เลขยกกำลัง เริ่มที่ 0

    # ใช้คำนวณส่วนที่เป็นทศนิยม
    result2 = 0     # เอาไว้เก็บค่าฐานสอง
    floor = 0       # เอาไว้เก็บค่า floor
    k = -1          # เลขยกกำลังของทศนิยม เริ่มที่ -1
    
    # คิดส่วนที่เป็นจำนวนเต็ม
    while (x_int / 2) > 0: 
        if (x_int / 2) - (x_int // 2) == 0:
            remainder = 0
            result1 = result1 + (remainder * (10 ** n))
            n += 1
        else:
            remainder = 1
            result1 = result1 + (remainder * (10 ** n))
            n += 1
        result1 = result1
        x_int = x_int // 2

    # คิดส่วนที่เป็นทศนิยม
    for i in range(6):
        if (x_float * 2) < 1:
            floor = 0
            result2 = result2 + (floor * (10 ** k))
            k -= 1
            x_float = (x_float * 2) 
        else:
            floor = 1
            result2 = result2 + (floor * (10 ** k))
            k -= 1
            x_float = (x_float * 2) - int(x_float * 2)
        result2 = result2
        x_float = x_float

    return result1 + result2

def main():
    x = float(input())
    print(float_to_bin(x))

if __name__ == '__main__':
    main()
