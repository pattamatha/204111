#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 08
# Problem 4
# 204111 Sec 001

import math

def main():
    nums = [1, 2, 3, 4]
    n = int(input())
    out = dest_rotate_list(nums, n)
    print(out)
    print(nums)
    
    '''
    print(nums) #[1, 2, 3, 4]
    out = dest_rotate_list(nums, n)
    print(out)  #None
    print(nums) #[4, 1, 2, 3]
    nums = [1, 2, 3, 4]
    n = -4
    print(nums) #[1, 2, 3, 4]
    out = dest_rotate_list(nums, n)
    print(out)  #None
    print(nums) #[2, 3, 4, 1]
    nums = [1, 2, 3, 4]
    n = 105
    print(nums) #[1, 2, 3, 4]
    out = dest_rotate_list(nums, n)
    print(out)  #None
    print(nums) #[4, 1, 2, 3]
    '''

# แบ่งเป็น 3 กรณี
# กรณีที่ n = 0, list_a จะไม่เปลี่ยนแปลง
# กรณีที่ n > 0, list_a ขยับไปทางขวา n ครั้ง
# กรณีที n < 0, list_a ขยับไปทางซ้าย n ครั้ง
def dest_rotate_list(nums, n):
    if n == 0:
        return nums    # แสดงว่าไม่มีการ rotate ก็ return nums ได้เลย
    elif n > 0:
        for i in range(n):                  
            store = nums[len(nums) - 1]     # ถ้า n > 0, store เอาไว้เก็บค่าตัวสุดท้าย ก่อนจะทำการลบ
            nums.pop(len(nums) - 1)         # ลบตัวสุดท้ายในลิสต์
            nums.insert(0, store)           # แทรก store ในตำแหน่งแรก(0)
    elif n < 0:
        for i in range(abs(n)):
            store = nums[0]                 # ถ้า n < 0, store เอาไว้เก็บค่าตัวแรก ก่อนจะทำการลบ
            nums.pop(0)                     # ลบตัวแรกในลิสต์
            nums.append(store)              # เพิ่ม store ในตำแหน่งสุดท้าย

if __name__ == '__main__':
    main()