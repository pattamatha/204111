#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 05
# Problem 2
# 204111 Sec 001

def max_number(x , y, z):           # Create a function for find max number to use in def in_p_triple(x, y, z)
    if x > y:
        if x > z:
            max_number = x 
        else:
            max_number = z
    else:
        if y > z:
            max_number = y 
        else:
            max_number = z
    return max_number

def is_p_triple(x, y, z):
    max_numbers = max_number(x, y, z)             # if we know max number of all three numbers, we can verify that is Pythagorean triple
    if x == max_numbers:                          # use Pythagorean triple equation to coding
        if (x ** 2) == (y ** 2) + (z ** 2):
            return True
        else:
            return False
    elif y == max_numbers:
        if (y ** 2) == (x ** 2) + (z ** 2):
            return True
        else:
            return False
    elif z == max_numbers:    
        if (z ** 2) == (y ** 2) + (x ** 2):
            return True
        else:
            return False

def main():
    x = int(input())
    y = int(input())
    z = int(input())
    print(is_p_triple(x, y, z))

if __name__ == '__main__':
    main()
