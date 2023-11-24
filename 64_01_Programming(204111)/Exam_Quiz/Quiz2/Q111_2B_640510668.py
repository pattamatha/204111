# !/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Quiz2 1/64
# Problem 2B
# 204111 Sec 001
 
def transpose_matrix(matrix):
    row = len(matrix)       # นับจำนวนแถวของ matrix
    col = len(matrix[0])    # นับจำนวนหลักของ matrix
    # สร้างmatrixเปล่า(ทุกตำแหน่งมีค่าเท่ากับ 0) ที่สลับหลักเป็นแถว สลับแถวเป็นหลัก
    matrix_zero = []
    for r in range(col):
        m = []
        for c in range(row):
            m.append(0)
        matrix_zero.append(m)
    # ทำการแทนค่าแต่ละหลักแต่ละแถวใน matrix zero ได้เลย
    for r in range(row):
        for c in range(col):
            # การ transpose คือการสลับหลักเป็นแถว สลับแถวเป็นหลัก
            # matrix_zero เป็นเมทริกซ์ที่จะใช้เก็บค่าที่transposeแล้ว จึงให้หลักเป็นแถวและให้แถวเป็นหลัก
            matrix_zero[c][r] = matrix[r][c]
    return matrix_zero

def main():
    m_list = [[9]]
    print(m_list)
    print(transpose_matrix(m_list))
    print(m_list)
    m_list = [[0, 2, -3]]
    print(m_list)
    print(transpose_matrix(m_list))
    print()
    m_list = [[-1, 4], [5, 6]]
    print(m_list)
    print(transpose_matrix(m_list))
    print()
    m_list = [[2, -3, 1], [0, 3, 5]]
    print(m_list)
    print(transpose_matrix(m_list))
    print()
    m_list = [[7], [0], [8]]
    print(m_list)
    print(transpose_matrix(m_list))
    print()
    m_list = [[6, 0], [0, -3], [1, 8]]
    print(m_list)
    print(transpose_matrix(m_list))
    print()

    # test cases
    m_list = [[7, -9, 0]]
    print(m_list)
    print(transpose_matrix(m_list))
    m_list = [[4, -1, 5], [3, 0, -2]]
    print(m_list)
    print(transpose_matrix(m_list))
    m_list = [[0], [0], [7]]
    print(m_list)
    print(transpose_matrix(m_list))
    m_list = [[5, -1], [-1, -2], [6, -3]]
    print(m_list)
    print(transpose_matrix(m_list))
    m_list = [[-8, -2], [0, 0]]
    print(m_list)
    print(transpose_matrix(m_list))
    m_list = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]
    print(m_list)
    print(transpose_matrix(m_list))
    m_list = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(m_list)
    print(transpose_matrix(m_list))


if __name__ == '__main__':
    main()
