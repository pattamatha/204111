#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 10
# Problem 4
# 204111 Sec 001

import string
import copy

def main():
	line = str(input())
	print(uniform(line))

def uniform(line):
	# ทำการลบ white space, number, punctuation เหลือเพียงอักษรภาษาอังกฤษ เพื่อใช้ในการตรวจสอบ
	line1 = copy.deepcopy(line)
	line1 = line.replace(" ", "")
	for i in string.digits:
		line1 = line1.replace(i, "")
	for i in string.punctuation:
		line1 = line1.replace(i, "")
	
	# นับจำนวนอักษรพิมพ์เล็ก และอักษรพิมพ์ใหญ่ เพื่อนำมาเปรียบเทียบกัน
	count_upper = 0
	count_lower = 0
	for l in line1:
		if l.isupper() == True:
			count_upper += 1
		else:
			count_lower += 1

	# ทำการแปลงตัวอักษรตามเงื่อนไข
	# ถ้าจำนวนตัวอักษรพิมพ์ใหญ่มากกว่า ให้แปลงเป็นพิมพ์ใหญ่ทั้งหมด
	if count_upper > count_lower:
		line = line.upper()
	# ถ้าจำนวนตัวอักษรพิมพ์เล็กมากกว่า ให้แปลงเป็นพิมพ์เล็กทั้งหมด
	elif count_upper < count_lower:
		line = line.lower()
	# ถ้าจำนวนตัวอักษรพิมพ์ใหญ่เท่ากับจำนวนตัวอักษรพิมพ์เล็ก ให้แปลงตามตัวอักษรตัวแรก
	else: #count_upper == count_lower:
		if line1[0].isupper() == True:
			line = line.upper()
		else:
			line = line.lower()
	return line

if __name__ == '__main__':
	main()