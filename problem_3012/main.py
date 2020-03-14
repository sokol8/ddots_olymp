# Contest 132 - https://labs.dots.org.ua/ddots/contests?id=132
# Problem 3012 - https://labs.dots.org.ua/ddots/problems?id=3012

import sys

def solve(number, debug) -> str:

	ERROR_MESSAGE = 'Error'

	modulus = number % 7
	if debug:
		print('%7 = {}'.format(modulus))

	if 0 < modulus: 
		raise ValueError(ERROR_MESSAGE)

	result = (number//7 - 27)

	modulus = number % 3
	if debug:
		print('%3 = {}'.format(modulus))

	if 0 < modulus: 
		raise ValueError(ERROR_MESSAGE)

	result = result // 3

	if debug:
		print(result)

	return result



# Get Input from STDIN
for line in sys.stdin:

	try:
		number = solve(int(line), False)
		print(number)
	except ValueError as error:
		print(error)
	
	sys.exit(0)

####
# 210 (X = 1)
# 399 (X = 3)
# 84 (X = -5)
# -2142 (X = -111)


