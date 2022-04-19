import numpy as np
import sys
sys.path.append('../')
from ex04.prediction import predict_ 

def loss_elem_(y, y_hat):
	output = [0.0 for i in range(len(y))]
	for i in range(len(y)):
		output[i] = (y_hat[i] - y[i]) ** 2
	return (np.array(output))

def loss_(y, y_hat):
	return (1/(2*len(y))) * np.sum(loss_elem_(y, y_hat))
