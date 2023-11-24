#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 03
# Problem 3
# 204111 Sec 001

def octagon_area(x):
    octagon_area = (x * x) - (((x / 3) * (x / 3)) * 2)
    return octagon_area

def main():
    # รับด้านจาก user
    x = int(input())
    # พิมพ์พื้นที่ของรูปแปดเหลี่ยมด้านเท่า
    print(octagon_area(x))

if __name__ == '__main__':
    main()
