#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ ลำดับที่ 20
# 640510668
# Lab Quiz 3
# Problem 2
# 204111 Sec 001

import re
def main():
	print(three_letters_count("eating Hating color"))
	print(three_letters_count("Wish you all good luck for the exam \nde"))

def three_letters_count(text):
	t1 = text.lower()	# ทำให้textกลายเป็นตัวอักษรพิมพ์เล็กทั้งหมด
	t1 = t1.rstrip()	# ลบwhite space ทางขวา
	t1 = t1.lstrip()	# ลบwhite space ทางซ้าย
	t1 = t1.split(" ")	# ทำการแบ่งคำด้วย space bar 
	# t = ['eating', 'hating', 'color'] => ตัวอย่างของt
	t = []
	for sub in t1:
		t.append(sub.replace('\n','')) # ทำการลบ \n

	# ทำการตัด 3-letters
	m = [] 
	for i in range(len(t)):   
		if len(t[i]) > 2: # กรณีที่คำมีความยาวมากกว่า 3 ตัวอักษร
			while len(t[i]) > 2: 
				m.append(t[i][:3]) 
				t[i] = t[i][1:] 
		elif len(t[i]) > 0 and len(t[i]) < 3: # กรณีที่คำมีความยาวมากกว่า 0 ตัวอักษร แต่น้อยกว่า 3 ตัวอักษร
			m.append(t[i])

	# พอได้ 3-letters ของแต่ละคำแล้ว จะนำมานับความถี่
	res = {}
	for item in m:
		if item in res:
			res[item] += 1
		else:
			res[item] = 1
	return res

if __name__ == '__main__':
	main()