#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 11
# Problem 5
# 204111 Sec 001

def main():
	list_x = [19,48,175,290,873,7,43,69]
	radix_int(list_x)
	print('--------')
	print(list_x)

def radix_int(list_x):
	list_x.sort()	# ใช้ sort() method เพื่อเรียงลำดับใน list_x

if __name__ == '__main__':
	main()