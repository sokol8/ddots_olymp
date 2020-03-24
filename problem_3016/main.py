# Contest 132 - https://labs.dots.org.ua/ddots/contests?id=132
# Problem 3015 - https://labs.dots.org.ua/ddots/problems?id=3015

import sys

def add_item_to_results(input_set, new_item) -> {}:
	if 0 <= new_item:
		input_set.add(new_item)
	return input_set


def generate_solution(input_set, debug) -> {}:

	results_set = set()

	for item in input_set:
		new_item = 0.0

		if 0 == item % 1: # item is integer 
			add_item_to_results(results_set, item - 0.5)
			add_item_to_results(results_set, item / 2)
		else: #item is not integer
			add_item_to_results(results_set, item - 0.5)

	if debug:
		print("results_set: {}".format(results_set))

	return results_set

def solve(items_count, iterations_count, debug) -> ():

	solutions_set = generate_solution({items_count}, debug)
	solutions_count = 1

	if debug:
		print("first solution: {}".format(solutions_set))

	while solutions_count < iterations_count:
		solutions_set = generate_solution(solutions_set, debug)
		solutions_count += 1

	if debug:
		print("solutions count: {}".format(solutions_count))

	solutions = ' '.join(str(s) for s in sorted(solutions_set))
	return (len(solutions_set), solutions)

# Get Input from STDIN
lines = []
DEBUG_MODE = False
DEVELOP_MODE = False


if DEVELOP_MODE:

	(solutions_count, solutions) = solve(10, 4, DEBUG_MODE)
	print(solutions_count)
	print(solutions)

else:
	for line in sys.stdin:
		input_array = [int(i) for i in line.rsplit(' ')]
		(solutions_count, solutions) = solve(input_array[0], input_array[1], DEBUG_MODE)
		print(solutions_count)
		print(solutions)
		sys.exit(0)






