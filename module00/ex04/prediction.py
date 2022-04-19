import numpy as np

def add_intercept(x):
	if type(x) != np.ndarray or len(x) < 1:
		return None
	if type(x[0]) != np.ndarray:
		x = x.reshape(-1, 1)
	output = [[0.0 for x in range(len(x[0]) + 1)] for y in range(len(x))]
	for i in range (len(x)):
		for j in range (len(x[0])):
			output[i][0] = 1.0
			output[i][j + 1] = x[i][j] 
	return(np.array(output))

def predict_(x, theta):
	assert type(x) == np.ndarray and len(x) > 1
	# for e in x:
		# assert isinstance(e, (int, float, complex, np.integer, np.float_))
	assert type(theta) == np.ndarray 
	# assert len(theta) == 2
	# for e in theta:
		# assert isinstance(e, (int, float, complex, np.integer, np.float_))
	X = add_intercept(x)
	if len(X[0]) != len(theta):
		return None
	return (np.matmul(X, theta))
