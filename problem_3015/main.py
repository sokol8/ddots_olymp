# Contest 132 - https://labs.dots.org.ua/ddots/contests?id=132
# Problem 3015 - https://labs.dots.org.ua/ddots/problems?id=3015

import sys


def splitInt(number, debug) -> []
	digits_array = []
	while 0 < number:
		digits_array.append(number % 10)
		number //= 10

	return digits_array[::-1]

# TEST NUMBERS AFTER DIVISION ON 42
# 1325374 => 1234
# 698772 => 
# 5163758
# 9898989

def decrypt(numer, debug) -> str:
		ERROR_RESPONSE = "????"

		if 0 != number % 42:
			if debug:
				print("{} % 42 = {}. Must be 0".format(number, number % 42))
			return ERROR_RESPONSE

		digits_array = splitInt(number)
		if debug:
			print("digits_array: {}".format(digits_array))

		if 7 != len(digits_array):
			if debug:
				print("Incorrect number {} length: {}".format(number, len(digits_array)))
			return ERROR_RESPONSE

		#### ANALYZE DIGITS HERE

		return ERROR_RESPONSE


def solve(numbers_array, debug) -> str:
	if 4 != len(numbers_array):
		raise ValueError("Invalid arguments number in numbers_array: {}".format(len(numbers_array)))

	decrypted_numbers_array = []
	for number in numbers_array:
		decrypted_number = decrypt(number)
		decrypted_numbers_array.append(decrypted_number)

		if debug:
			print("decrypted: {}".format(decrypted_number))

	solution = " ".join(decrypted_numbers_array)

	if debug:
		print("solution: {}".format(solution))

	return solution


# Get Input from STDIN
lines = []
DEBUG_MODE = True
DEVELOP_MODE = True

if DEVELOP_MODE:

	numbers_array = [55665708, 29348432, 216877836, 415757538]
	solution = solve(numbers_array, DEBUG_MODE)

else:
	for line in sys.stdin:
		lines.append(int(line))

		if 4 == len(lines):
			numbers_array = [int(line) for line in lines]
			solution = solve(numbers_array, DEBUG_MODE)
			print(solution)
			sys.exit(0)



