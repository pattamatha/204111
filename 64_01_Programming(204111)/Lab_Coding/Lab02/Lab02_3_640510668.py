#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 02
# Problem Linear EQ
# 204111 Sec 001

print("First Equation")
mi = float(input("Input m1: "))     				#mi is m1
bi = float(input("Input b1: "))     				#bi is b1
print("Second Equation")
mii = float(input("Input m2: "))    				#mii is m2
bii = float(input("Input b2: "))    				#bii is b2
x = (bii - bi) / (mi - mii)							# หาค่า x จากสมการ y = mx + b 
y = ((bi * mii) - (bii * mi)) / (mii - mi)			# หาค่า x จากสมการ y = mx + b 
print("The point of intersection is at x = %.2f and y = %.2f" %(x,y))