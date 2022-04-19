import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('../')
from ex03.tools import add_intercept
from ex04.prediction import predict_

def plot(x, y, theta):
	plt.scatter(x, y)
	plt.plot(predict_(x, theta))
	plt.show()
