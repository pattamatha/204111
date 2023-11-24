# test 3

import string
def main():
	print(patterned_message("123","** *** ** ** *"))\
	
	'''
	print(patterned_message("D and C",'''\
***************
******   ******
***************\
	'''))
	print(patterned_message("Three Diamonds!",'''\
  *     *     *
 ***   ***   ***
***** ***** *****
 ***   ***   ***
  *     *     *\
	'''))


def patterned_message(message, pattern):
	for i in pattern:
		if i == " ":
			print(i, end = "")

if __name__ == '__main__':
	main()