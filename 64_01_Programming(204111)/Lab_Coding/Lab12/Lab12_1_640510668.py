#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 12
# Problem 1
# 204111 Sec 001

def main():
	x = int(input("x: "))
	y = int(input("y: "))
	print(gcd(x, y))

"""def gcd(x, y):
	if y == 0: # Base case
		return x
	else:	# recursion
		r = x % y
		x = y
		y = r 
		return gcd(x, y)"""

def gcd(x, y):
	if x%y == 0: # Base case
		return y
	else:	# recursion
		return gcd(abs(y), abs(x)%y)

if __name__ == '__main__':
	main()