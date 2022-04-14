import numpy as np

class TinyStatistician:
	def mean(self, input):
		if type(input) != list and type(input) != np.array and len(input) < 1:
			return None
		for i in range(len(input)):
			assert type(input[i]) == int or type(input[i] == float)
		return sum(elem for elem in input) / len(input)

a = [1, 42, 300, 10, 59]
print(TinyStatistician().mean(a))
