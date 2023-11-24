#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 02
# Problem Temperature
# 204111 Sec 001

f = int(input("Input temperature in Fahrenheit: "))                 # f is temperature in Fahrenheit
c = 5 * ((f - 32) / 9)												# c is temperature in Celsius
print("%.2f degree Fahrenheit is %.2f degree Celsius" % (f,c))