#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 11
# Problem 4
# 204111 Sec 001

def main():
	p1 = [(2, 6), (1, 34), (0, -8)]
	p2 = [(2, -6), (0, 2), (1, 1)]
	print(polynomial_addition(p1, p2))

def polynomial_addition(p1, p2):
	dictp1 = dict(sorted(p1))
	dictp2 = dict(sorted(p2))
	# ทำการบวกสัมประสิทธิ์ที่มีเลขยกกำลังเท่ากัน
	res = dict(dictp1)	# res เอาไว้เก็บคำตอบหลังจากการบวกสัมประสิทธิ์
	res.update(dictp2)	# update res ให้มีตัวยกกำลังใน p2 ที่ p1 ยังไม่มี เพื่อที่จะสามารถทำการบวกได้
	for power1, coe1 in dictp1.items():
		for power2, coe2 in dictp2.items():
			if power1 == power2: # ถ้าเลขยกกำลังเท่ากันให้ทำการบวกสัมประสิทธิ์จของ p1,p2
				res[power1] = coe1 + coe2
	# เมื่อทำการบวกเลขสัมประสิทธิ์ของแต่ละเลขยกกำลังเรียบร้อย จะทำการแปลงจาก dict ให้กลายเป็น tuple ที่อยู่ใน list
	res2 = {}
	for power, coe in res.items():
		if coe != 0: # เราจะทำการแสดงค่าแค่สัมประสิทธิ์ของเลขยกกำลังที่ไม่เป็น 0
			res2[power] = coe
	result = list(reversed(sorted(res2.items())))
	return result

if __name__ == '__main__':
	main()