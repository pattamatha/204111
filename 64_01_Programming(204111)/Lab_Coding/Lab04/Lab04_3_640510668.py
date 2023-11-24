#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 04
# Problem 3
# 204111 Sec 001

def calculate_p2p_evolve_exp(p, c):
    # WRITE YOUR CODE HERE
    evolve = ((p - 1) + c) // 12           # evolve is max number of times that can be changed pidgey to pidgeotto
    if p == 0 and c == 0:
        return 0
    elif p > evolve or p == evolve:
        return evolve * 500
    elif p < evolve:
        return p * 500
    elif p <= 12 and c == 0:
        return 0
    elif p == 0 and c <= 12:
        return 0
    elif p >= 13 and c == 0:
        return evolve * 500
    elif p == 0 and c >= 13:
        return 0
    else:
        pass

def main():
    # receive input from user
    p = int(input())
    c = int(input())
    # print result from function
    print(calculate_p2p_evolve_exp(p, c))

if __name__ == '__main__':
    main()
