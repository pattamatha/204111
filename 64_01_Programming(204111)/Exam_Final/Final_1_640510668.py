#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ ลำดับที่ 20
# 640510668
# Lab Final
# Problem 1
# 204111 Sec 001

def main():
	'''
	print(is_in_q1((2, 7, 1.5)))		# a
	print(is_in_q1((3.2, 2.5, 4.06)))	# b
	print(is_in_q1((-5.5, -4.5, 2.5)))	# c
	print(is_in_q1((2, -5.2, 3)))		# d
	print(is_in_q1((7.2, -2.8, 1.2)))	# e

	print(is_in_q2((2, 7, 1.5)))		# a
	print(is_in_q2((3.2, 2.5, 4.06)))	# b
	print(is_in_q2((-5.5, -4.5, 2.5)))	# c
	print(is_in_q2((2, -5.2, 3)))		# d
	print(is_in_q2((7.2, -2.8, 1.2)))	# e

	print(is_in_q3((2, 7, 1.5)))		# a
	print(is_in_q3((3.2, 2.5, 4.06)))	# b
	print(is_in_q3((-5.5, -4.5, 2.5)))	# c
	print(is_in_q3((2, -5.2, 3)))		# d
	print(is_in_q3((7.2, -2.8, 1.2)))	# e

	print(is_in_q4((2, 7, 1.5)))		# a
	print(is_in_q4((3.2, 2.5, 4.06)))	# b
	print(is_in_q4((-5.5, -4.5, 2.5)))	# c
	print(is_in_q4((2, -5.2, 3)))		# d
	print(is_in_q4((7.2, -2.8, 1.2)))	# e
	'''

	list_a = [(2, 7, 1.5),(3.2, 2.5, 4.06),(-5.5, -4.5, 2.5),(2, -5.2, 3), (7.2, -2.8, 1.2)]
	print(count_segment(list_a))

def is_in_q1(circle):
	if circle[0] > 0 and circle[1] > 0:
		return True
	else:
		return False

def is_in_q2(circle):
	left = circle[0] - circle[2]	# ตรวจสอบจุดด้านซ้ายของทุกวงกลม 
	if left < 0 and circle[1] > 0:	# ถ้าจุดด้านซ้ายมีค่าน้อยกว่า0 และแกนYมากกว่า0 แสดงว่า มีจุดที่อยู่ใน q2
		return True
	else:
		return False

def is_in_q3(circle):
	left = circle[0] - circle[2]	# ตรวจสอบจุดด้านซ้ายของทุกวงกลม 
	if left < 0 and circle[1] < 0:	# ถ้าจุดด้านซ้ายมีค่าน้อยกว่า0 และแกนYน้อยกว่า0 แสดงว่า มีจุดที่อยู่ใน q3
		return True
	else:
		return False

def is_in_q4(circle):
	bot = circle[1] - circle[2]		# ตรวจสอบจุดด้านล่างของทุกวงกลม
	left = circle[0] - circle[2]	# ตรวจสอบจุดด้านซ้ายของทุกวงกลม 
	right = circle[0] + circle[2]	# ตรวจสอบจุดด้านขวาของทุกวงกลม
	if right > 0 and circle[1] < 0:	# ถ้าจุดด้านขวามีค่ามากกว่า0 และแกนYน้อยกว่า0 แสดงว่า มีจุดที่อยู่ใน q4
		return True
	elif bot < 0 and circle[0] > 0:	# ถ้าจุดด้านล่างมีค่าน้อยกว่า0 และแกนXมากกว่า0 แสดงว่า มีจุดที่อยู่ใน q4
		return True
	else:
		return False

def count_segment(list_a):
	q1 = 0
	q2 = 0
	q3 = 0
	q4 = 0
	res = []
	for cir in list_a:
		if is_in_q1(cir) == True:
			q1 += 1
	res.append(q1)
	for cir in list_a:
		if is_in_q2(cir) == True:
			q2 += 1
	res.append(q2)
	for cir in list_a:
		if is_in_q3(cir) == True:
			q3 += 1
	res.append(q3)
	for cir in list_a:
		if is_in_q4(cir) == True:
			q4 += 1
	res.append(q4)
	return tuple(res)

if __name__ == '__main__':
	main()