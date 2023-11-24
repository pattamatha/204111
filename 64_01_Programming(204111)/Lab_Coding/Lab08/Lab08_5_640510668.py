#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 08
# Problem 5
# 204111 Sec 001

import string

def main():
    n = int(input())
    '''
    print(num_to_word(1000000))
    print(num_to_word(200000000))
    print(num_to_word(9000000))
    print(num_to_word(1000000000))
    print(num_to_word(9000000000))
    print(num_to_word(10000000000))
    print(num_to_word(80000000000))
    print(num_to_word(700000000000))
    print(num_to_word(1489662012))
    '''
    print(num_to_word(n))

''' 
เลข 1-3 หลัก, 0 < num <= 999 แบ่งเป็น 3 กรณี
กรณีที่ 1 num < 20 : ให้อ่านตาม unit_list ได้เลย
กรณีที่ 2 num >= 20 and num <= 99 : ถ้าหลักหน่วยเป็น 0 ให้อ่านตาม tens_list, ถ้าหลักหน่วยเป็นเลข 1-9 ให้อ่าน tens_list + unit_list
กรณีที่ 3 num >= 100 and num <= 999: ถ้าหลักสิบและหลักหน่วยเป็น 0 ให้อ่านตาม unit_list hundred, ถ้าหลักสิบ+หน่วย < 20 ให้อ่าน 
                                    unit_list hundred(หลักร้อย) + unit_list(หลักหน่วย+สิบ),
                                    ถ้าหลักสิบ+หน่วย >= 20 ให้ดูหลักหน่วย ถ้าเป็น 0 ให้อ่าน unit_list hundred(หลักร้อย) + tens_list(หลักหน่วย+สิบ) 
                                    ถ้าไม่เป็น 0 ให้อ่าน unit_list hundred(หลักร้อย) + tens_list(หลักสิบ) + unit_list(หลักหน่วย)
'''
def three_digits_to_word(n):
    #วิธีอ่านหลักหน่วย
    unit_list = ["", "one", "two", "three", "four", "five",
                 "six", "seven", "eight", "nine", "ten",
                 "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                 "sixteen", "seventeen", "eighteen", "nineteen"]
    #วิธีอ่านหลักสิบ
    tens_list = ["", "", "twenty", "thirty", "forty", "fifty",
                 "sixty", "seventy", "eighty", "ninety"]
    if n < 20:
        return unit_list[n]
    elif n >= 20 and n <= 99: 
        dm = divmod(n, 10) #dm is divmod
        div = dm[0]
        mod = dm[1]
        if mod == 0:
            return tens_list[div]
        else: # mod != 0
            return tens_list[div] + "-" + unit_list[mod]
    elif n >= 100 and n <= 999:
        dm = divmod(n, 100) #dm is divmod
        div = dm[0]
        mod = dm[1]
        if mod == 0:
            return unit_list[div] + " " + "hundred"
        elif mod < 20:
            return unit_list[div] + " " + "hundred" + " " + unit_list[mod]
        elif mod >= 20:
            mod = divmod(mod, 10)
            mod1 = mod[0]
            mod2 = mod[1]
            if mod2 == 0:
                number = tens_list[mod1]
            else: # mod != 0
                number = tens_list[mod1] + "-" + unit_list[mod2]
            return unit_list[div] + " " + "hundred" + " " + number

def num_to_word(n):
    if n == 0:
        return 'zero'
    elif 0 < n <= 999:
        return three_digits_to_word(n)
    elif 999 < n <= 999999:
        # สมมติตัวเลข 12345
        n1 = n % 1000 #345
        n = n // 1000 #12
        number1 = three_digits_to_word(n)
        n = n1
        number2 = three_digits_to_word(n)
        return number1 + " " + "thousand" + " " + number2
    elif 999999 < n <= 999999999:
        # สมมติตัวเลข 12345678
        # 10000010
        n1 = n % 1000000    # 345678
        n = n // 1000000    # 12
        number1 = three_digits_to_word(n)
        n2 = n1 % 1000      # 678
        n = n1 // 1000      # 345
        number2 = three_digits_to_word(n)
        n = n2
        number3 = three_digits_to_word(n)
        if n1 // 1000 != 0: # คือช่วงของ thousand ถ้ามีก็return number1,2,3 ถ้าไม่มี ให้return number1,3
            return number1 + " " + "million" + " " + number2 + " " + "thousand" + " " + number3
        else:
            return number1 + " " + "million" + " " + number3
    elif 999999999 < n <= 999999999999:
        # สมมติตัวเลข 1234567891
        n1 = n % 1000000000 #234567891
        n = n // 1000000000 #1
        number1 = three_digits_to_word(n)
        n2 = n1 % 1000000 #567891
        n = n1 // 1000000 #234
        number2 = three_digits_to_word(n)
        n3 = n2 % 1000 #891
        n = n2 // 1000 #567
        number3 = three_digits_to_word(n)
        n = n3  #891
        number4 = three_digits_to_word(n)
        if n1 // 1000000 != 0 and n2 // 1000 != 0:
            return number1 + " " + "billion" + " " + number2 + " " + "million" + " " + number3 + " " + "thousand" + " " + number4
        elif n1 // 1000000 != 0 and n2 // 1000 == 0:
            return number1 + " " + "billion" + " " + number2 + " " + "million" + " " + number4
        elif n1 // 1000000 == 0 and n2 // 1000 == 0:
            return number1 + " " + "billion" + " " + number4
    
if __name__ == '__main__':
    main()