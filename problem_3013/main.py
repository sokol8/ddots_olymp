# Contest 132 - https://labs.dots.org.ua/ddots/contests?id=132
# Problem 3013 - https://labs.dots.org.ua/ddots/problems?id=3013

import sys

def solve(number, target, debug) -> str:

	if number <= target:
		return ''

	if target < 0 or number < 0:
		return ''		

	DIVIDE_STEP = ":2"
	DECREASE_STEP = "-1"

	solution = []

	while target < number:

		if debug:
			print('start of loop number : {}'.format(number))

		if 0 == number % 2:
			number /= 2

			if  number < target: # overshoot
				number *= 2
				number -= 1
				solution.append(DECREASE_STEP)
				if debug:
					print('rollback divide by 2. Decrease by -1: {}'.format(number))
			else:
				solution.append(DIVIDE_STEP)

				if debug:
					print('divide by 2: {}'.format(number))

				if number == target:
					break

		else: 
			number -= 1
			solution.append(DECREASE_STEP)
			if debug:
				print('decrease by -1: {}'.format(number))

	if debug:
		print("final number = {}".format(number))

	return '\n'.join(solution)


# Get Input from STDIN
lines = []
DEBUG_MODE = False
for line in sys.stdin:
		lines.append(int(line))
		if 2 == len(lines):
			solution = solve(lines[0], lines[1], DEBUG_MODE)
			print(solution)
			sys.exit(0)
	
	


