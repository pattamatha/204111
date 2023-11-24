#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 10
# Problem 1
# 204111 Sec 001

import string
def main():
    n = int(input("enter n (3≤n≤25): "))
    sep = input("sep: ")
    if sep == "":
        print(square_frame(n, sep=' '))
    else:
        sep = str(sep)
        print(square_frame(n, sep))

def square_frame(n, sep=' '):
    sep = str(sep)
    # n = 5
    list_a = [] # สร้างlistเปล่า(ที่เป็นstrเปล่าๆ เอาไว้ใช้แทนที่)
    for r in range(n):  
        m = []
        for c in range(n):
            m.append("")
        list_a.append(m)
    start = 0   # เริ่มต้นลูปที่ 0
    end = n-1   # ลูปจะสิ้นสุดที่ n-1
    count = int((n+1)/2) # จำนวนสี่เหลี่ยมที่จะวน 
    num = 1     # เลขจะเริ่มที่ 01
    for i in range(count): # ทำการแทนที่ตัวเลข
        if i == 0: #จะทำการวนแค่สี่เหลี่ยมนอกสุด
            for j in range(start, end+1):
                if num < 10:
                    list_a[i][j] = "0" + str(num)
                else:
                    list_a[i][j] = str(num)
                num += 1
            for j in range(start+1, end+1):
                if num < 10:
                    list_a[j][end] = "0" + str(num)
                else:
                    list_a[j][end] = str(num)
                num += 1
            for j in range(end-1, start-1, -1):
                if num < 10:
                    list_a[end][j] = "0" + str(num)
                else:
                    list_a[end][j] = str(num)
                num += 1
            for j in range(end-1, start, -1):
                if num < 10:
                    list_a[j][start] = "0" + str(num)
                else:
                    list_a[j][start] = str(num)
                num += 1
            start = start + 1
            end = end - 1
        else:   # จะทำการวนสี่เหลี่ยมที่เหลือด้านใน ซึ่งสี่เหลี่ยมด้านในคือsepทั้งหมด 
            for j in range(start, end+1):
                list_a[i][j] = sep + sep
            for j in range(start+1, end+1):
                list_a[j][end] = sep + sep
            for j in range(end-1, start-1, -1):
                list_a[end][j] = sep + sep
            for j in range(end-1, start, -1):
                list_a[j][start] = sep + sep
            start = start + 1
            end = end - 1
    final2 = []
    for i in range(len(list_a)):
        for j in range(len(list_a[i])):
            final1 = sep.join(list_a[i])
        final2.append(final1)
    for i in range(len(final2)):
        final = "\n".join(final2)
    print(final)

if __name__ == '__main__':
    main()