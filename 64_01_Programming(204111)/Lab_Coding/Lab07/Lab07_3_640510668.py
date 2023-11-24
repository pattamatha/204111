#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 07
# Problem 3
# 204111 Sec 001

def main():
    n = int(input())
    triangle(n)

def triangle(n):
    # บรรทัดแรกจะมี * 1 ตัวเสมอ
    print("*")
    
    # ทำตั้งแต่บรรทัดที่2 ถึงบรรทัดที่ n-1
    for i in range(n - 2):
        for j in range(i + 1):
            if j == 0:
                print("*", end = ".")
            else:
                print(".", end = ".")
        print("*")
    
    # บรรทัดสุดท้ายจะมี * n ตัวเสมอ
    for i in range(n - 1):
        print("*", end = " ")  # print * ออกมา n - 1 ตัว และช่องว่างต่อท้าย
    print("*")                 # print * ออกมา 1 ตัว และไม่มีช่องว่างต่อท้าย


if __name__ == '__main__':
    main()
