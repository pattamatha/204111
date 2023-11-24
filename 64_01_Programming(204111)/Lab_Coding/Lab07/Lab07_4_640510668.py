#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 07
# Problem 4
# 204111 Sec 001

def main():
    n = int(input())
    print(life_path(n))


def life_path(n):
    result = 0      # เพื่อเก็บผลลัพธ์ในแต่ละครั้งที่คำนวณ
    for i in (str(n)):  #เปลี่ยน n ให้เป็น string เพื่อให้ i แสดงตัวเลขแต่ละตัวใน n
        result = result + int(i)   
        if result >= 10:    # กรณีที่ result มีค่ามากกว่า 10 ต้องนำมาคำนวณอีกครั้ง
            result = (result % 10) + (result // 10)
        else: #result < 10
            result = result
    return result


if __name__ == '__main__':
    main()