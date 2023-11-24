#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 13
# Problem 1
# 204111 Sec 001

def main():
	square_matrix([[2, 3, 4, 3], [1, 2, 3, 5]])
	square_matrix([[1, 2], [1, 2, 3], [1, 2], [1, 2], [1], [2]])
	square_matrix([[1, 2, 3, 4], [1, 2], [3], [1, 4, 4]])

def square_matrix(list_x):
	# นับจำนวนแถวและหลัก
	rows = len(list_x)
	col = []
	for r in range(len(list_x)):
		count = 0
		for c in range(len(list_x[r])):
			count += 1
		col.append(count)
	cols = max(col)

	if cols > rows:
		item = []
		for i in range(cols):
			item.append(0)
		for i in range(cols-rows):
			list_x.append(item)
		for i in range(cols):
			while len(list_x[i]) < cols:
				list_x[i].append(0)

	else: #cols <= rows
		for i in range(rows):
			while len(list_x[i]) < rows:
				list_x[i].append(0)

if __name__ == '__main__':
	main()