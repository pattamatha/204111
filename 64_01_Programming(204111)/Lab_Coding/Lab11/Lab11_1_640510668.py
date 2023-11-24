#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 11
# Problem 1
# 204111 Sec 001

def main():
	list_x = ["11/1/2100","5/12/1999","19/1/2003","11/9/2001"]
	sort_date(list_x)
	print("---")
	print(list_x)

def sort_date(list_x):
	for i in range(len(list_x)):
		date_str = list_x[i]
		date_list = date_str.split("/")
		date_tup = list(date_list[::-1])
		if len(date_tup[1]) == 1: #ถ้าเดือนเป็นเลขที่น้อยกว่า 10 ให้เติม 0 ด้านหน้า
			date_tup[1] = "0" + date_tup[1]
		if len(date_tup[2]) == 1: ##ถ้าวันเป็นเลขที่น้อยกว่า 10 ให้เติม 0 ด้านหน้า
			date_tup[2] = "0" + date_tup[2]
		list_x[i] = date_tup

	list_x.sort()

	for i in range(len(list_x)):
		date_tup = list_x[i]
		if date_tup[1][0] == "0":
			date_tup[1] = date_tup[1][1]
		if date_tup[2][0] == "0":
			date_tup[2] = date_tup[2][1]
		date_str = "/".join(date_tup[::-1])
		list_x[i] = date_str

if __name__ == '__main__':
	main()