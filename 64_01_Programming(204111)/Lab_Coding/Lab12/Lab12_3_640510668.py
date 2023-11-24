#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 12
# Problem 3
# 204111 Sec 001

# ทำกับเพื่อนรหัส 640510627 ค่ะ

def main():
	n = int(input("input n: "))
	print(is_prime(n))

def is_prime(n, div = 2):
	# base case
	if n == 2:
		return True
	if n % div == 0:
		return False
	if (div * div) > n:
		return True

	# recursion
	else:
		return is_prime(n, div + 1)

if __name__ == '__main__':
	main()