#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ ลำดับที่ 20
# 640510668
# Lab Quiz 3
# Problem 1
# 204111 Sec 001

def main():
	print(subset({'a', 'b', 'c'}, 2))
	print(subset({'d', 's', 'c', 'x'}, 5))
	print(subset({'a', 'b', 'c'}, 0))

def subset(set_a, n):
	num = len(set_a)
	if n == 0:
		return [set()]
		
	elif n <= num:
		set_a = list(set_a)
		# ขั้นตอนการสร้าง subset 
		lists = [set()] #ให้listsมี listเปล่า(แทนsetว่าง)ไว้ข้างในเพื่อเป็นตัวเริ่มต้น(subsetจะมีsetว่างเสมอ)
		for i in set_a:
			for j in lists:
				lists = lists + [list(j)+[i]]
		# ขั้นตอนนี้จะตรวจสอบว่าจำนวนของsubsetแต่ละตัวนั้น มีค่าเกิน n หรือไม่ ถ้าเกิน เราจะไม่เพิ่มลงใน res(คำตอบสุดท้าย)
		res = []
		for i in range(len(lists)):
			if len(lists[i]) <= n:
				res.append(set(lists[i]))
		return res

	elif n > num:
		set_a = list(set_a)
		# ขั้นตอนการสร้าง subset 
		lists = [set()] #ให้listsมี listเปล่า(แทนsetว่าง)ไว้ข้างในเพื่อเป็นตัวเริ่มต้น(subsetจะมีsetว่างเสมอ)
		for i in set_a:
			for j in lists:
				lists = lists + [list(j)+[i]]
		# ขั้นตอนนี้คือการเพิ่มsubsetทุกตัวลงในres(คำตอบสุดท้าย) เพราะnเกินจำนวนของsubsetเลยใส่subsetทั้งหมด
		res = []
		for i in lists:
			res.append(set(i))
		return res

if __name__ == '__main__':
	main()