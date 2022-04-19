import numpy as np
import sys
sys.path.append('../')
from ex03.tools import add_intercept

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
