#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 09
# Problem 5
# 204111 Sec 001

def main():
	x = str(input())
	p = [(2, -6), (0, -8), (1, 34)]
	print(print_polynomial(p, x))

def print_polynomial(p, x):
	poly = list(reversed(sorted(p)))
	# poly1 คือจำนวนเลขยกกำลัง
	# poly2 คือสัมประสิทธิ์หน้าตัวแปร
	poly1,poly2 = zip(*p)
	
if __name__ == '__main__':
	main()