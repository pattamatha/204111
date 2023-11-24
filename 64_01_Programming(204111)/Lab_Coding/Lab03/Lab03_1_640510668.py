#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 03
# Problem 1
# 204111 Sec 001

def main():
   # รับข้อมูลพื้นที่ผิวจาก user
   surface_area = float(input("input surface area: "))
   # นำพื้นที่ผิวที่ได้มาคำนวณหารัศมี
   radius = find_r_from_surface_area(surface_area)
   # นำรัศมีที่คำนวณได้มาคำนวณหาปริมาตร
   volume = sphere_volume(radius)
   # แสดงปริมาตรทรงกลม
   print("volume = {0:.2f}".format(volume))

import math

def find_r_from_surface_area(surface_area):
    radius = (surface_area / ((math.pi) * 4)) ** 0.5
    return radius


def sphere_volume(radius):
    volume = 4/3*math.pi*radius**3
    return volume


if __name__ == '__main__':
    main()
