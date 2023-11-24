#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 08
# Problem 3
# 204111 Sec 001

import math

def main():
    list_a = [1,2,3,4]
    n = int(input())
    print(nondest_rotate_list(list_a, n))

    '''
    n = 1
    print(nums)  #[1, 2, 3, 4]
    print(nondest_rotate_list(nums, n))   #[4, 1, 2, 3]

    n = 105
    print(nums)  #[1, 2, 3, 4]
    print(nondest_rotate_list(nums, n))  #[4, 1, 2, 3]

    n = -1
    print(nums)  #[1, 2, 3, 4]
    print(nondest_rotate_list(nums, n))  #[2, 3, 4, 1]
    '''

# แบ่งเป็น 3 กรณี
# กรณีที่ n = 0, list_a จะไม่เปลี่ยนแปลง
# กรณีที่ n > 0, list_a ขยับไปทางขวา n ครั้ง
# กรณีที n < 0, list_a ขยับไปทางซ้าย n ครั้ง
def nondest_rotate_list(list_a, n):
    if n == 0:
        return list_a
    elif n > 0:
        pos = (len(list_a) - (n % len(list_a))) # pos is position, หาตำแหน่งเพื่อ slicing
        n1 = list_a[:pos]                       # n1 คือ ตำแหน่งที่อยู่ก่อนหน้า pos
        n2 = list_a[pos:]                       # n2 คือ ตำแหน่งที่อยู่หลัง pos
        return n2 + n1      
    elif n < 0:
        pos = abs(n) % len(list_a)  # pos is position, หาตำแหน่งเพื่อ slicing 
        n1 = list_a[:pos]           # n1 คือ ตำแหน่งที่อยู่ก่อนหน้า pos
        n2 = list_a[pos:]           # n2 คือ ตำแหน่งที่อยู่หลัง pos
        return n2 + n1

if __name__ == '__main__':
    main()