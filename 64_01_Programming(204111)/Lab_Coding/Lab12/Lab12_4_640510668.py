#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 12
# Problem 4
# 204111 Sec 001

def main():
	n = int(input("n: "))
	print(series(n))

def series(n):
	# base case
	if n == 0:
		return 0
	if n == 1:
		return 1

	# recursion
	else:
		# n is even number
		if n % 2 == 0: 
			return (series(n-1) * 2) + 1
		# n is odd number
		else:
			return (series(n-1) * 2) - 1

if __name__ == '__main__':
	main()