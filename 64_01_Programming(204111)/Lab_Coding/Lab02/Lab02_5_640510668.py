#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 02
# Problem Fibonacci
# 204111 Sec 001

n = int(input("Enter n: "))
g = ((1 + (5**0.5)) /  2)          # g is Golden Ratio
fi = ((g**n)/(5**0.5)+0.5)         # fi is Fibonacci
print("fib(%d) = %d" %(n,fi))