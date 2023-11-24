import math

def base_b(x,b):
    if x==0:
        return 0
    r = x % b
    result = r + (10 * base_b(x//b,b))
    return result

def main():
    x=int(input("x:"))
    b=int(input("b:"))

    print(base_b(x,b))

main()