#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 08
# Problem 1
# 204111 Sec 001

import string

def main():
    str1 = str(input())
    str2 = str(input())
    print(is_anagram(str1, str2))

def is_anagram(str1, str2):
    # change to lowercase letters for easy check
    str1 = str1.lower()
    str2 = str2.lower()
    # remove white space
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    # remove number(0-9)
    for i in string.digits:
        str1 = str1.replace(i, "")
        str2 = str2.replace(i, "")
    # remove punctuation
    for i in string.punctuation:
        str1 = str1.replace(i, "")
        str2 = str2.replace(i, "")
    # arrange the letters to compare
    str1 = sorted(list(str1))
    str2 = sorted(list(str2))
    
    if str1 == str2:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
