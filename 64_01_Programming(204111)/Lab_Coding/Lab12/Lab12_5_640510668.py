#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 12
# Problem 5
# 204111 Sec 001

def main():
	num = int(input("input num: "))
	print(reverse_num(num))

def reverse_num(num):
	# base case
	if num == 0 :
		return 0
		
	# recursion
	d = num % 10	# เก็บค่าหลักสุดท้ายมาคำนวณ
	# (d * (10 ** (len(str(num)) - 1))) ส่วนนี้คือการนำหลักสุดท้าย มาแปลง(คำนวณ)ให้กลายเป็นหลักแรก
	# reverse_num(num // 10) เรียกใช้ฟังก์ชันอีกครั้งโดยอัพเดตค่า num (ค่า num ที่ลบหลักสุดท้ายออกแล้ว จนหมดทุกหลัก)
	rev = (d * (10 ** (len(str(num)) - 1))) + reverse_num(num // 10)
	return rev

if __name__ == '__main__':
	main()