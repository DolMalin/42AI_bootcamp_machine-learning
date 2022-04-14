import numpy as np
import math

def check_input(input):
	if type(input) != list and type(input) != np.array and len(input) < 1:
		return False
	return True

def format_list(input):
	if type(input) != np.ndarray:
		input = np.array(input)
	input = input.flatten()
	for e in input:
		assert isinstance(e, (int, float, complex, np.integer, np.float_))
	return input

def	get_mean(input):
	return sum(elem for elem in input) / len(input)

def get_median(input):
	input.sort()
	if (len(input) % 2 == 0):
		return (input[(math.floor(len(input) / 2))] + input[(math.floor(len(input) / 2)) - 1]) / 2
	return float(input[math.floor(len(input) / 2)])

# def	recursive_mean(input):
# 	if type(input[0]) != list and type(input[0]) != np.ndarray:
# 		for e in input:
# 			assert isinstance(e, (int, float, complex, np.integer, np.float_))
# 		return get_mean(input)
# 	return recursive_mean([list_mean(e) for e in input])

class TinyStatistician:

	def mean(self, input):
		if not check_input(format_list(input)):
			return None
		return get_mean(format_list(input))

	def median(self, input):
		if not check_input(format_list(input)):
			return None
		return get_median(format_list(input))


b = np.array([1, 42, 300, 10, 59])
c = np.array([[[2.0, 3.0, 4.0] ,[5.0, 6.0, 8.0], [4, 6, 9]], [[2.0, 3.0, 4.0] ,[5.0, 6.0, 8.0], [4, 6, 9]]])

a = [2, 4, 8]

print(np.median(a))
print(TinyStatistician().median(a))