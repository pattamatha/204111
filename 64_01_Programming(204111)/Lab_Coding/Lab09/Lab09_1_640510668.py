#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 09
# Problem 1
# 204111 Sec 001

def main():
	# m1 from user
	print("m1 from user")
	row_m1 = int(input("row m1: "))	
	col_m1 = int(input("col m1: "))
	m1 = [[int(input("number: ")) for c in range(col_m1)] for r in range(row_m1)]
	# m2 from user
	print("m2 from user")
	row_m2 = int(input("row m2: "))	
	col_m2 = int(input("col m2: "))
	m2 = [[int(input("number: ")) for c in range(col_m2)] for r in range(row_m2)]
	print(" ")
	print(m1)
	print(m2)
	print(matrix_mult(m1, m2))

def matrix_mult(m1, m2):
	rows_m1 = len(m1)		# นับแถวของ m1
	rows_m2 = len(m2)		# นับแถวของ m2
	cols_m1 = len(m1[0])	# นับหลักของ m1 (สำหรับเมทริกซ์ ทุกแถวมีจำนวนหลักเท่ากัน จึงนับแค่แถวแรกได้เลย)
	cols_m2 = len(m2[0])	# นับหลักของ m2 

	if cols_m1 == rows_m2:	  # เมทริกซ์ 2 เมทริกซ์คูณกันได้(จำนวนหลักของ m1 == จำนวนแถวของ m2), เมทริกซ์ขนาด ixk คูณกับ kxj จะได้เมทริกซ์ขนาด ixj
		m = 0
		n = []
		for i in range(rows_m1):
			for j in range(cols_m2):
				m = 0
				for k in range(rows_m2):
					m += (m1[i][k]) * (m2[k][j])
				n += [m] 
		# เราได้ผลลัพธ์มาแล้วอยู่ในn แต่nเป็น list1D ดังนั้นเราจะมาทำให้มันกลายเป็น list2D ขนาด ixj
		matrix1 = []	# เอาไว้เก็บ matrix ขนาด ixj
		count = 0		# เอาไว้รันตำแหน่ง n
		for r in range(rows_m1):
			matrix2 = []
			for c in range(cols_m2):
				matrix2.append(n[count])
				count += 1
			matrix1.append(matrix2)
		return matrix1
	else: #cols_m1 != rows_m2:  # เมทริกซ์ 2 เมทริกซ์คูณกันไม่ได้(จำนวนหลักของ m1 != จำนวนแถวของ m2)
		return None

if __name__ == '__main__':
    main()