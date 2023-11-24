#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 11
# Problem 3
# 204111 Sec 001

import math

def main():
	print(prime_factor(34))
	print(coprime_factor(48, 180))

def prime_factor(n):
	if n == 0 or n == 1:
		return []
	else: # n > 1
		fac = []
		div = 2	# ตัวประกอบเฉพาะจะเริ่มที่ 2
		num = n # ใช้ num เป็นตัวกำหนดขอบเขตของตัวประกอบ
		while div <= math.sqrt(num) + 1:
			if n % div == 0:
				fac.append(div)
				n = n // div
			else:
				div += 1
		if div > math.sqrt(num) + 1 and n > 1:
			fac.append(n)
	return fac

def coprime_factor(a, b):
	list_a = prime_factor(a)
	list_b = prime_factor(b)
	#list_a = [2, 2, 3, 3, 5]
	#list_b = [2, 2, 2, 2, 3]
	count_a = {}	# นับความถี่ของตัวประกอบเฉพาะแต่ละตัวใน list_a
	for c in list_a:
		if c in count_a:
			count_a[c] += 1
		else:
			count_a[c] = 1
	count_b = {}	# นับความถี่ของตัวประกอบเฉพาะแต่ละตัว list_b
	for c in list_b:
		if c in count_b:
			count_b[c] += 1
		else:
			count_b[c] = 1
	# count_a = {2: 2, 3: 2, 5: 1}
	# count_b = {2: 4, 3: 1}
	inter = count_a.keys() & count_b.keys() # หาส่วนที่ intersection ของ count_a และ count_b
	result = []
	for num in inter:
		if count_a[num] > count_b[num]: # เวลาที่จะหาส่วนที่ซ้ำกัน เราจะเอาตัวที่ซ้ำกัน จำนวนที่น้อยที่สุดจากlistใดlistนึง
			result.extend([num] * count_b[num])
		else: # ในกรณีที่มีตัวซ้ำเท่ากัน สามารถใช้จำนวนตัวซ้ำจากlistใดก็ได้
			result.extend([num] * count_a[num])
	result.sort() # เรียงลำดับจากน้อยไปมากด้วย
	return result

if __name__ == '__main__':
	main()