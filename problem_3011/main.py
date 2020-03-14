# Contest 132 - https://labs.dots.org.ua/ddots/contests?id=132
# Problem 3011 - https://labs.dots.org.ua/ddots/problems?id=3011

import sys

def solve(number, debug) -> int:
	accumulator = 0
	position = 0

	while 0 < number:
		digit1 = number % 10
		number //= 10

		if 0 == number:
			accumulator += digit1 * (10 ** position)
			
			if debug:
				print('pre-final: {}'.format(accumulator))

			accumulator *= 42
			break

		digit2 = number % 10
		digitSumRemainder = (digit1 + digit2) % 10

		accumulator += digit1 * (10 ** position)
		position += 1

		accumulator += digitSumRemainder * (10 ** position)
		position += 1

		if debug:
			print(digit1)
			print(digit2)
			print('>> {}'.format(digitSumRemainder))
			print(': {}'.format(accumulator))
			print('-----')
		
	if debug:
		print('final: {}'.format(accumulator))

	return accumulator


# Get Input from STDIN
for line in sys.stdin:
	number = solve(int(line), False)
	print(number)
	sys.exit(0)

# DEBUG
# number = 1289
number = 1010
print('hello world: {}'.format(number))

solve(number, True)
