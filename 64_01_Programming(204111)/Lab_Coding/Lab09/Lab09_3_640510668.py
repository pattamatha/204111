#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 09
# Problem 3
# 204111 Sec 001

def main():
	# board from user
	n = int(input("row and col: "))
	board = [[int(input("number: ")) for c in range(n)] for r in range(n)]
	print(board)
	print(is_magic_square(board))

# สร้าง def number_in_board(board) เพื่อตรวจสอบเลขที่ซ้ำกันใน board
def number_in_board(board):
	num = []
	for i in range(len(board)):
		for j in board[i]:
			num += [j]
	number = []
	for k in num:
		if k not in number:
			number += [k]
	
	if len(num) == len(number):
		return True
	else:
		return False

def is_magic_square(board):
	square = number_in_board(board)
	if square == True:
		#ตรวจสอบแถว
		test = sum(board[0]) # เอาsumของแถวแรกเป็นตัวทดสอบ 
		for i in range(len(board)):
			test == sum(board[i]):
				return True
			else:
				return False

	else: #square == False:
		return False

if __name__ == '__main__':
	main()