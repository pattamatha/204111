#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 10
# Problem 2
# 204111 Sec 001

import string

def main():
	x = int(input("enter x: "))
	b = int(input("enter b: "))
	print("{} base {} is palindrome ?" .format(x,b))
	print(is_palindrome(x, b))

def is_palindrome(x, b):
	# ทำการแปลง x จากฐาน 10 เป็นฐาน b
	num = []
	while x // b > 0:	# ลูปนี้จะทำการหารไปเรื่อยๆ จนถึงผลหารก่อนสุดท้าย(ผลหารยังไม่เป็น0)
		num.insert(0, str(x % b))
		x = x // b
	num.insert(0, str(x % b)) # ดังนั้นจะต้องทำการหารอีกครั้ง จนผลหารเป็น 0 ถึงจะเสร็จสิ้นขั้นตอนการแปลงเลขฐาน
	x_base = "".join(num)	  # x_base คือ x ที่แปลงเป็นเลขฐาน b เรียบร้อย

	# ตรวจสอบว่าเป็น palindrome ไหม จาก x ที่เป็นฐาน b แล้ว 
	# ทำการแบ่งครึ่ง x โดย x1 คือ x ส่วนหน้า, x2 คือ x ส่วนหลัง(ที่ทำการกลับด้าน) => เพื่อที่เราจะนำ x1,x2 มาเปรียบเทียบกันว่าเท่ากันหรือไม่
	index = len(x_base) // 2 	# index คือ จำนวนความยาวของx1,x2จากการแบ่งครึ่งของ x และยังใช้เป็นตำแหน่งในการแบ่งครึ่ง x
	if len(x_base) % 2 == 0:
		x1 = x_base[:index]
		x2 = x_base[index:]
		x2 = x2[::-1]	# ทำการกลับด้าน x2
	else:
		x1 = x_base[:index]
		x2 = x_base[index+1:]
		x2 = x2[::-1]	# ทำการกลับด้าน x2

	count = 0	# ค่า count เอาไว้นับ เมื่อ x1 เท่ากับ x2 ในแต่ละตำแแหน่ง
	for i in range(len(x1)):
		if x1[i] == x2[i]:
			count += 1
		else:
			count += 0

	if count == index:	# ถ้า x1 เท่ากับ x2, จำนวนcountจะเท่ากับจำนวนความยาวของx1,x2จากการแบ่งครึ่งของ x
		return True
	else:
		return False

if __name__ == '__main__':
	main()