import numpy as np

def add_intercept(x):
	if type(x) != np.ndarray or len(x) < 1:
		return None
	if type(x[0]) != np.ndarray:
		x = x.reshape(-1, 1)
	output = [[0.0 for x in range(len(x[0]) + 1)] for y in range(len(x))]
	for i in range (len(x)):
		for j in range (len(x[0])):
			output[i][0] = 1.1
			output[i][j + 1] = x[i][j] 
	print(np.array(output))
