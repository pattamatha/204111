#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 08
# Problem 2
# 204111 Sec 001


def classify(list_x):
    list_a = []
    list_b = []
    list_c = []

 #เขียนโค้ดลงไปตรงนี้
    for x in list_x:            # ตรวจสอบแต่ละตัวใน list_x
        if type(x) == int:      # หากค่า x มีtype เป็น int ให้เก็บค่าใน list_a
            list_a += [x]
        elif type(x) == float:  # หากค่า x มีtype เป็น float ให้เก็บค่าใน list_b
            list_b += [x]
        elif type(x) == str:    # หากค่า x มีtype เป็น str ให้เก็บค่าใน list_c
            list_c += [x]

#ในpython เราสามารถ return ได้มากกว่า 1 ค่า โดยผลลัพธ์จะถูกมัดรวมออกไปเป็นค่าเดียวซึ่งมี type เป็น  Tuple
    return list_a, list_b, list_c

def main():
    x = [10, 'he4>lo', 23.5, 4]
    list_int, list_float, list_string = classify(x)
    print(type(list_int), list_int)
    print(type(list_float), list_float)
    print(type(list_string), list_string)

#<class 'list'> [10, 4]
#<class 'list'> [23.5]
#<class 'list'> ['he4>lo']


if __name__ == '__main__':
    main()
