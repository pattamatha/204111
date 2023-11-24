#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 02
# Problem Millisecond
# 204111 Sec 001

millisec = int(input("Input number of milliseconds: "))		# millisec is millisecoonds
day = millisec // 86400000
millisec = millisec % 86400000
hour = millisec // 3600000
millisec = millisec % 3600000
minute = millisec // 60000
millisec = millisec % 60000
sec = millisec // 1000										# sec is second
millisec = millisec % 1000
print("Results = %d day(s), %d hour(s), %d minute(s), %d second(s), and %d millisec(s)" %(day,hour,minute,sec,millisec))