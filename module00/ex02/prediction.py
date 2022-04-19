import numpy as np

def simple_predict(x, theta):
	assert type(x) == np.ndarray and len(x) > 1
	for e in x:
		assert isinstance(e, (int, float, complex, np.integer, np.float_))
	assert type(theta) == np.ndarray 
	assert len(theta) == 2
	for e in theta:
		assert isinstance(e, (int, float, complex, np.integer, np.float_))
	output = [0.0 for x in range(len(x))]
	for i in range(len(output)):
		output[i] = float(theta[1] * x[i] + theta[0])
	return (np.array(output))
