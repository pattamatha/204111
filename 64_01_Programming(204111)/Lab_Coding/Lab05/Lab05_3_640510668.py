#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 05
# Problem 3
# 204111 Sec 001

# 3 case about this
# first case is calculate in leap year and next year isn't leap year
# second case is calculate in normal year and next year isn't leap year
# third case is calculate in normal year and next year is leap year

# about leap year
# leap year => February has 29 days
# normal year => February has 28 days

def leap_year(y):                # This is function for checking wheater year is leap year or not
    if y % 4 == 0:              
        if y % 400 == 0:        
            return True
        elif y % 100 == 0:
            return False
        else:
            return True
    else:
        return False

def next_leap_year(y):          # This is function for cheaking wheater next year is a leap year or not
    y = y + 1
    if y % 4 == 0:              
        if y % 400 == 0:        
            return True
        elif y % 100 == 0:
            return False
        else:
            return True
    else:
        return False

def count_down_to_songkran(d, m, y):
    leap_y = leap_year(y)
    next_y = next_leap_year(y)

    # number of days in each month
    d_m1 = 31
    d_m2 = 29  # for easy calculation, I think February has 29 days
    d_m3 = 31
    d_m4 = 30
    d_m5 = 31
    d_m6 = 30
    d_m7 = 31
    d_m8 = 31
    d_m9 = 30
    d_m10 = 31
    d_m11 = 30
    d_m12 = 31

    if leap_y == True:       # first case is calculate in leap year and next year isn't leap year
        if m < 4:
            if m == 1:
                return (d_m1 - d) + d_m2 + d_m3 + 13
            if m == 2:
                return (d_m2 - d) + d_m3 + 13
            if m == 3:
                return (d_m3 - d) + 13
        elif m == 4:
            if m == 4 and d < 13:
                return 13 - d
            elif m == 4 and d == 13:
                return 0
            elif m == 4 and d > 13:
                return (d_m4 - d) + d_m5 + d_m6 + d_m7 + d_m8 + d_m9 + d_m10 + d_m11 + d_m12 + d_m1 + (d_m2 - 1) + d_m3 + 13
        elif m > 4:
            if m == 5:
                return (d_m5 - d) + d_m6 + d_m7 + d_m8 + d_m9 + d_m10 + d_m11 + d_m12 + d_m1 + (d_m2 - 1) + d_m3 + 13
            if m == 6:
                return (d_m6 - d) + d_m7 + d_m8 + d_m9 + d_m10 + d_m11 + d_m12 + d_m1 + (d_m2 - 1) + d_m3 + 13
            if m == 7:
                return (d_m7 - d) + d_m8 + d_m9 + d_m10 + d_m11 + d_m12 + d_m1 + (d_m2 - 1) + d_m3 + 13
            if m == 8:
                return (d_m8 - d) + d_m9 + d_m10 + d_m11 + d_m12 + d_m1 + (d_m2 - 1) + d_m3 + 13
            if m == 9:
                return (d_m9 - d) + d_m10 + d_m11 + d_m12 + d_m1 + (d_m2 - 1) + d_m3 + 13
            if m == 10:
                return (d_m10 - d) + d_m11 + d_m12 + d_m1 + (d_m2 - 1) + d_m3 + 13
            if m == 11:
                return (d_m11 - d) + d_m12 + d_m1 + (d_m2 - 1) + d_m3 + 13
            if m == 12:
                return (d_m12 - d) + d_m1 + (d_m2 - 1) + d_m3 + 13
    else:
        if next_y == False:     # second case is calculate in normal year and next year isn't leap year
            if m < 4:
                if m == 1:
                    return (d_m1 - d) + (d_m2 - 1) + d_m3 + 13
                if m == 2:
                    return ((d_m2 - 1) - d) + d_m3 + 13
                if m == 3:
                    return (d_m3 - d) + 13
            elif m == 4:
                if m == 4 and d < 13:
                    return 13 - d
                elif m == 4 and d == 13:
                    return 0
                elif m == 4 and d > 13:
                    return (d_m4 - d) + d_m5 + d_m6 + d_m7 + d_m8 + d_m9 + d_m10 + d_m11 + d_m12 + d_m1 + (d_m2 - 1) + d_m3 + 13
            elif m > 4:
                if m == 5:
                    return (d_m5 - d) + d_m6 + d_m7 + d_m8 + d_m9 + d_m10 + d_m11 + d_m12 + d_m1 + (d_m2 - 1) + d_m3 + 13
                if m == 6:
                    return (d_m6 - d) + d_m7 + d_m8 + d_m9 + d_m10 + d_m11 + d_m12 + d_m1 + (d_m2 - 1) + d_m3 + 13
                if m == 7:
                    return (d_m7 - d) + d_m8 + d_m9 + d_m10 + d_m11 + d_m12 + d_m1 + (d_m2 - 1) + d_m3 + 13
                if m == 8:
                    return (d_m8 - d) + d_m9 + d_m10 + d_m11 + d_m12 + d_m1 + (d_m2 - 1) + d_m3 + 13
                if m == 9:
                    return (d_m9 - d) + d_m10 + d_m11 + d_m12 + d_m1 + (d_m2 - 1) + d_m3 + 13
                if m == 10:
                    return (d_m10 - d) + d_m11 + d_m12 + d_m1 + (d_m2 - 1) + d_m3 + 13
                if m == 11:
                    return (d_m11 - d) + d_m12 + d_m1 + (d_m2 - 1) + d_m3 + 13
                if m == 12:
                    return (d_m12 - d) + d_m1 + (d_m2 - 1) + d_m3 + 13
        if next_y == True:      # third case is calculate in normal year and next year is leap year
            if m < 4:
                if m == 1:
                    return (d_m1 - d) + (d_m2 - 1) + d_m3 + 13
                if m == 2:
                    return ((d_m2 - 1) - d) + d_m3 + 13
                if m == 3:
                    return (d_m3 - d) + 13
            elif m == 4:
                if m == 4 and d < 13:
                    return 13 - d
                elif m == 4 and d == 13:
                    return 0
                elif m == 4 and d > 13:
                    return (d_m4 - d) + d_m5 + d_m6 + d_m7 + d_m8 + d_m9 + d_m10 + d_m11 + d_m12 + d_m1 + d_m2 + d_m3 + 13
            elif m > 4:
                if m == 5:
                    return (d_m5 - d) + d_m6 + d_m7 + d_m8 + d_m9 + d_m10 + d_m11 + d_m12 + d_m1 + d_m2 + d_m3 + 13
                if m == 6:
                    return (d_m6 - d) + d_m7 + d_m8 + d_m9 + d_m10 + d_m11 + d_m12 + d_m1 + d_m2 + d_m3 + 13
                if m == 7:
                    return (d_m7 - d) + d_m8 + d_m9 + d_m10 + d_m11 + d_m12 + d_m1 + d_m2 + d_m3 + 13
                if m == 8:
                    return (d_m8 - d) + d_m9 + d_m10 + d_m11 + d_m12 + d_m1 + d_m2 + d_m3 + 13
                if m == 9:
                    return (d_m9 - d) + d_m10 + d_m11 + d_m12 + d_m1 + d_m2 + d_m3 + 13
                if m == 10:
                    return (d_m10 - d) + d_m11 + d_m12 + d_m1 + d_m2 + d_m3 + 13
                if m == 11:
                    return (d_m11 - d) + d_m12 + d_m1 + d_m2 + d_m3 + 13
                if m == 12:
                    return (d_m12 - d) + d_m1 + d_m2 + d_m3 + 13

def main():
    d = int(input())
    m = int(input())
    y = int(input())
    print(count_down_to_songkran(d, m, y))


if __name__ == '__main__':
    main()
