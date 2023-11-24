import math

def main():
	n = int(input("enter n: "))
	print(left_max(n))

def left_max(n):
	if n<10:
		return n
	else: 
		first = n // (10**(int(math.log10(n))))
		num = n % (10**(int(math.log10(n))))
		second = num // (10**(int(math.log10(num))))
		
		if first>=second:
			num = (n % (10**(int(math.log10(num))-2))) + first*(10**(int(math.log10(num))-1))
			result = fisrt + left_max(num)
		else:
			num = (n % (10**(int(math.log10(num))-2))) + second*(10**(int(math.log10(num))-1))
			result = second + left_max(num)

		return result
main()