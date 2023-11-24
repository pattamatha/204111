#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 12
# Problem 2
# 204111 Sec 001

def main():
	n = int(input("base n: "))
	num = int(input("num: "))
	print(n_base_to_10(n,num))

def n_base_to_10(n, num):
	# base case
	if num == 0:
		return 0
	if num == 1:
		return 1

	# recursion
	length = len(str(num)) # นับความยาวของ num เพื่อนำมาใช้คำนวณเลขยกกำลังในโค้ด
	power = pow(10, length - 1) # ใช้หาหลักแรกของ num และใช้อัพเดต num หลักที่เหลือ
	first = num // power # หลักแรกของ num (num ที่อัพเดตค่าแล้ว)
	# (pow(n, length - 1) * first) ตรงนี้คือส่วนที่คำนวณค่าที่แปลงจากฐานสิบเป็นฐานสองในแต่หลัก เริ่มที่หลักแรกของ num
	# n_base_to_10(n, num % power) เรียกใช้ฟังก์ชันอีกครั้งโดยอัพเดตค่า num (ค่า num ที่ลบหลักแรกออกแล้ว จนหมดทุกหลัก) 
	dec_result = (first * pow(n, length - 1)) + n_base_to_10(n, num % power) 
	return dec_result

if __name__ == '__main__':
	main()