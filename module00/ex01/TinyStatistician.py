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

def q_pos(input, q):
	return (len(input)) * q

def get_quartile(input):
	input.sort()
	print(input)
	q1 = input[math.floor(q_pos(input, 0.25))] if len(input) % 2 != 0 \
	else (input[math.floor(q_pos(input, 0.25))] + input[math.floor(q_pos(input, 0.25)) - 1]) / 2 
	q3 = input[math.floor(q_pos(input, 0.75))] if len(input) % 2 != 0 \
	else (input[math.floor(q_pos(input, 0.75))] + input[math.floor(q_pos(input, 0.75)) - 1]) / 2
	return (q1, q3)

class TinyStatistician:

	def mean(self, input):
		if not check_input(format_list(input)):
			return None
		return get_mean(format_list(input))

	def median(self, input):
		if not check_input(format_list(input)):
			return None
		return get_median(format_list(input))

	def quartile(self, input):
		if not check_input(format_list(input)):
			return None
		return get_quartile(format_list(input))


b = np.array([1, 42, 300, 10, 59])
c = np.array([[[2.0, 3.0, 4.0] ,[5.0, 6.0, 8.0], [4, 6, 9]]])
d = np.array([14, 15, 16, 17, 30, 32,  40, 44, 50, 52, 55, 57])

a = [1, 42, 300, 10, 59]


f = [[14, 17, 12, 33, 44],   
       [15, 6, 27, 8, 19],  
       [23, 2, 54, 1, 4 ]]

print(TinyStatistician().mean(a))
# print(np.quantile(a, 1/4), np.quantile(a, 3/4))

