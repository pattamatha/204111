#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 05
# Problem 5
# 204111 Sec 001

def element(year):                              # Create element function for use in zodiac_element function
    if year%10 == 0 or year%10 == 1:
        return 'Metal'
    elif year%10 == 2 or year%10 == 3:
        return 'Water'
    elif year%10 == 4 or year%10 == 5:
        return 'Wood'
    elif year%10 == 6 or year%10 == 7:
        return 'Fire'
    elif year%10 == 8 or year%10 == 9:
        return 'Earth'

def zodiac_element(year):
    elements = element(year)
    if year % 12 == 0:
        return (elements + ' Monkey')
    elif year % 12 == 1:
        return (elements + ' Rooster')
    elif year % 12 == 2:
        return (elements + ' Dog')
    elif year % 12 == 3:
        return (elements + ' Pig')
    elif year % 12 == 4:
        return (elements + ' Rat')
    elif year % 12 == 5:
        return (elements + ' Ox')
    elif year % 12 == 6:
        return (elements + ' Tiger')
    elif year % 12 == 7:
        return (elements + ' Rabbit')
    elif year % 12 == 8:
        return (elements + ' Dragon')
    elif year % 12 == 9:
        return (elements + ' Snake')
    elif year % 12 == 10:
        return (elements + ' Horse')
    elif year % 12 == 11:
        return (elements + ' Goat')

def main():
    year = int(input())
    print(zodiac_element(year))


if __name__ == '__main__':
    main()
