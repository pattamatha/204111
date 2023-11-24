#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 09
# Problem 2
# 204111 Sec 001

import copy
import math

def main():
	# matrix from user
	rows = int(input("row: "))
	cols = int(input("col: "))
	list_a = [[int(input("number: ")) for c in range(cols)] for r in range(rows)]
	# row and column to remove
	row = int(input("row to remove: "))
	col = int(input("colums to remove: "))
	# result
	print(list_a)
	print(remove_row_col(list_a, row, col))

def remove_row_col(list_a, row, col):
	rows = len(list_a)		# นับแถวของ list_a
	cols = len(list_a[0])	# นับหลักของ list_a (สำหรับเมทริกซ์ ทุกแถวมีจำนวนหลักเท่ากัน จึงนับแค่แถวแรกได้เลย)
	# พิจารณา row
	if row >= 0:
		if row >= rows:		# มี = ด้วย เพราะ rows เริ่มที่ 1, แต่ row เริ่มที่ 0
			matrix = copy.deepcopy(list_a)
		else: #abs(row) < rows:
			matrix = copy.deepcopy(list_a)
			matrix.pop(row)
	else: #row < 0:
		if abs(row) > rows:
			matrix = copy.deepcopy(list_a)
		else: #abs(row) <= rows:
			matrix = copy.deepcopy(list_a)
			matrix.pop(row)
	# พิจารณา colums
	if col >= 0:
		if col >= cols:		# มี = ด้วย เพราะ cols เริ่มที่ 1, แต่ cow เริ่มที่ 0
			matrix = matrix
		else: #abs(col) < cols:
			for i in range(len(matrix)):
				matrix[i].pop(col)
	else: #col < 0:
		if abs(col) > cols:
			matrix = matrix
		else: #abs(col) <= cols:
			for i in range(len(matrix)):
				matrix[i].pop(col)
	return matrix

if __name__ == '__main__':
	main()