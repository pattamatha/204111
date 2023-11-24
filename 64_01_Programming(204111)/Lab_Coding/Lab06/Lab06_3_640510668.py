#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 06
# Problem 3
# 204111 Sec 001

import math

def is_prime(num):
    div = 2
    while div <= math.sqrt(num) + 1:
        if num % div == 0:
            return False
        else:
            if div == 2:
                div = 3
            else:
                div += 1
    return True
    
def factorize(num):
    prime = is_prime(num)
    loop = 0
    if prime == True:
        if num == 0:
            print("0 is 0")
        elif num == 1:
            print("1 is 1")
        else:
            print(num,"is prime")
    elif num == 2:
        print(num,"is prime")
    else: #prime == False
        n = 2      #ค่าเริ่มต้น(จำนวนเฉพาะ)
        print(num, "is", end = " ")
        while n <= int(math.sqrt(num)):
            if num % n == 0:
                print(n, "*", end = " ")
                num = num // n
            elif num % n != 0:
                n += 1
            loop += 1
        if loop >= 1:
            print(num)

def main():
    num = int(input())
    factorize(num)

if __name__ == '__main__':
    main()
