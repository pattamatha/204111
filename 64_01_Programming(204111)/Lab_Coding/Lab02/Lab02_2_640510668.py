#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 02
# Problem BMI
# 204111 Sec 001

height = float(input("Input height (m): "))
weight = float(input("Input weight (kg): "))
bmi = weight / height**2							# bmi is Body Mass Index
print("BMI is %.4f" % bmi)