# test quiz
matrix = [[-1,4,2,2],[5,6,1,1]]
row = len(matrix)	#2
col = len(matrix[0])#3
#matrix_zero = [[0 for c in range(row)] for r in range(col)]
matrix_zero = []
for r in range(col):
	m = []
	for c in range(row):
		m.append(0)
	matrix_zero.append(m)

print(matrix_zero)