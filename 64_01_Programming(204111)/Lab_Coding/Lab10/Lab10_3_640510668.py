#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 10
# Problem 3
# 204111 Sec 001

import string
def main():
	patterned_message("123","** *** ** ** *")

	patterned_message("D and C",'''
***************
******   ******
***************
''')

	patterned_message("Three Diamonds!",'''
  *     *     *
 ***   ***   ***
***** ***** *****
 ***   ***   ***
  *     *     *
''')

def patterned_message(message, pattern):
	message = message.replace(" ", "")	#ทำการลบ white space(เพราะ white space ไม่นำมาเรียงบรรทัด)
	count = 0 # เอาไว้วนตัวอักษรใน message
	for i in pattern:
		if i == " ":
			print(" ", end = "")
		elif i == "\n":
			print("\n", end = "")
		elif i == "*":
			print(message[count], end = "")
			count += 1
			if count == len(message):
				count = 0

if __name__ == '__main__':
	main()