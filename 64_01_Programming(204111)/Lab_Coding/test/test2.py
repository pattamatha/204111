# test2

def crossed_number(n):
    for i in range(n): # loop each line
        for j in range(n): # loop each column
            if j == i or j == n-i: # condition for printing number
                print(j+1, end=" ") # print number
            else:
                print(" ", end=" ") # print space
        print("") # newline

n = int(input("Enter n: "))
crossed_number(n)