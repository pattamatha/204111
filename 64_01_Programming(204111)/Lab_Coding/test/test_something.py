# test_recursion_plus

# 
def main():
	n = int(input())
	print(plus(n))

def plus(n):
	if n == 1:
		return 1
	return n + plus(n-1)

if __name__ == '__main__':
	main()