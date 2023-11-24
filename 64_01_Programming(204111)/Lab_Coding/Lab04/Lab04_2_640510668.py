#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 04
# Problem 2
# 204111 Sec 001

def my_max_mid_min(a, b, c):
    # WRITE YOUR CODE HERE
    if a > b:
        max_number = a 
        min_number = b 
    else:
        max_number = b 
        min_number = a 
    if c > max_number:
        max_number = c 
    if c < min_number:
        min_number = c 
    mid_number = a + b + c - max_number - min_number
                
    print("max = %d" %max_number)
    print("mid = %d" %mid_number)
    print("min = %d" %min_number)

def main():
    # receive input from user
    a = int(input())
    b = int(input())
    c = int(input())
    # call function
    my_max_mid_min(a, b, c)

if __name__ == '__main__':
    main()
