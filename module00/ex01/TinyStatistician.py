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

def get_quantile(input, p):
	input.sort()
	if len(input) % 2 != 0:
		return input[math.floor(q_pos(input, p))]
	else:
		 return (input[math.floor(q_pos(input, p))] + input[math.floor(q_pos(input, p)) - 1]) / 2 

def get_quartile(input):
	input.sort()
	return (get_quantile(input, 0.25), get_quantile(input, 0.75))


def get_variance(input):
	return sum((e - get_mean(input)) ** 2 for e in input) / len(input)

def get_standard_deviation(input):
	return math.sqrt(get_variance(input))

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

	def percentile(self, input, p):
		if not check_input(format_list(input)):
			return None
		return get_quantile(format_list(input), p)

	def var(self, input):
		if not check_input(format_list(input)):
			return None
		return get_variance(format_list(input))

	def std(self, input):
		if not check_input(format_list(input)):
			return None
		return get_standard_deviation(input)
