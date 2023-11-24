#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 06
# Problem 5
# 204111 Sec 001


def longest_digit_run(n):
    count = 1   # ค่าเก็บเอาไว้เทียบ
    max_n = 0   # ค่าตัวที่ติดกันมากที่สุด
    n_str = str(n) #เปลี่ยนค่า n ให้เป็น string

    for i in range(len(n_str)):     #ใช้ฟังก์ชัน len ในการนับจำนวน เพื่อนำไปใช้ในการกำหนดจำนวนลูป
        if n % 10 == (n // 10) % 10: #เปรียบเทียบหลักที่ i และ i-1
            count += 1
            if max_n < count:
                max_n = count
            else:
                max_n = max_n
        else:
            count = 1
            if max_n < count:
                max_n = count
            else:
                max_n = max_n
        n = n // 10
    return max_n

    
def main():
    n = int(input())
    print(longest_digit_run(n))

if __name__ == '__main__':
    main()
