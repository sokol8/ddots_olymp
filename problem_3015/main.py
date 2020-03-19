# Contest 132 - https://labs.dots.org.ua/ddots/contests?id=132
# Problem 3015 - https://labs.dots.org.ua/ddots/problems?id=3015

import sys


def split_int(number, debug) -> []:
	digits_array = []
	while 0 < number:
		digits_array.append(int(number % 10))
		number //= 10

	return digits_array[::-1]

# TEST NUMBERS AFTER DIVISION ON 42
# 1325374 => 1234 // 1 3 2 5 3 7 4
# 698772 => 
# 5163758
# 9898989

def verify_triad(triad_array, debug) -> bool:
	if 3 != len(triad_array):
		if debug:
			print("incorrect array length: {}".format(len(triad_array)))
		return false
	return (triad_array[0] + triad_array[2]) % 10 == triad_array[1]

def decrypt(number, debug) -> str:
		ERROR_RESPONSE = "????"

		if 0 != number % 42:
			if debug:
				print("{} % 42 = {}. Must be 0".format(number, number % 42))
			return ERROR_RESPONSE

		number /= 42
		digits_array = split_int(number, debug)
		if debug:
			print("digits_array: {}".format(digits_array))

		if 7 != len(digits_array):
			if debug:
				print("Incorrect number {} length: {}".format(number, len(digits_array)))
			return ERROR_RESPONSE

		response_array = []
		
		# digits_array = [1, 3, 2, 5, 3, 7, 4]
		# digits_array[0:3] = [1, 3, 2]
		# digits_array[2:5] = [2, 5, 3]
		# digits_array[4:7] = [3, 7, 4]

		for i in [0, 2, 4]:
			if verify_triad(digits_array[i : i + 3], debug):
				response_array.append(str(digits_array[i]))
			else:
				if debug:
					print("Failed verifyig [{}:{}] triad = {} ".format(i, i + 3, digits_array[i : i + 3]))
				return ERROR_RESPONSE

		response_array.append(str(digits_array[6]))
		if debug:
			print("response_array = {} ".format(i, i + 3, response_array[i : i + 3]))

		return "".join(response_array)


def solve(numbers_array, debug) -> str:
	if 4 != len(numbers_array):
		raise ValueError("Invalid arguments number in numbers_array: {}".format(len(numbers_array)))

	decrypted_numbers_array = []
	for number in numbers_array:
		decrypted_number = decrypt(number, debug)
		decrypted_numbers_array.append(decrypted_number)

		if debug:
			print("decrypted: {}".format(decrypted_number))

	solution = " ".join(decrypted_numbers_array)

	if debug:
		print("solution: {}".format(solution))

	return solution


# Get Input from STDIN
lines = []
DEBUG_MODE = False
DEVELOP_MODE = False

if DEVELOP_MODE:

	numbers_array = [55665708, 29348432, 216877836, 415757538]
	solution = solve(numbers_array, DEBUG_MODE)
	print(solution)

else:
	for line in sys.stdin:
		lines.append(int(line))

		if 4 == len(lines):
			numbers_array = [int(line) for line in lines]
			solution = solve(numbers_array, DEBUG_MODE)
			print(solution)
			sys.exit(0)



