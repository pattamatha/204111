#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 06
# Problem 4
# 204111 Sec 001


def main():
    # ด้านล่างเป็นแค่โครงสำหรับการแสดงผล นักศึกษาสามารถเขียนเพิ่มหรือแก้ไขตามความเหมาะสม
    total = int(input("Total students: "))
    print('Enter score:')

    #กำหนดค่าต่างๆ
    max_num = 0         # ใช้เปรียบเทียบและเก็บค่า max score
    runner = 0          # ใช้เปรียบเทียบและเก็บค่า runner up
    score_all = 0       # ใช้เก็บคะแนนทั้งหมด เพื่อนำไปคำนวณหาค่า average

    for i in range(total):
        score = int(input())
        if total > 2:
            if score > max_num:
                max_num = score
            elif score < max_num:
                max_num = max_num
                if score > runner:
                    runner = score
                else:
                    runner = runner
        elif total == 2:
            if score > max_num:
                max_num = score
            elif score < max_num:
                max_num = max_num
            elif score < max_num and score != runner:
                runner = score
            elif score == max_num:
                max_num = max_num
                runner = None
        elif total == 1:
            max_num = score
            runner = None
        score_all += score

    average = score_all / total

    print('---')
    print('Max score is: %.2f' %max_num)
    if runner == None:
        print('Runner up is: None')
    else:
        print('Runner up is: %.2f' %runner)
    print('Average is: %.2f' %average)

if __name__ == '__main__':
    main()
