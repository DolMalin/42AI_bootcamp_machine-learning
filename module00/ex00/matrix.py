# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdal-mol <dolmalinn@gmail.com>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/12 10:54:32 by pdal-mol          #+#    #+#              #
#    Updated: 2022/04/12 18:26:57y pdal-mol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# ============== ~ UTILS ~ ============== #

def	create_matrix(row, col):
	return [[0.0 for x in range (col)] for y in range (row)]

def	align_row(matrix, row):
	return [matrix[x][row] for x in range(len(matrix))]

def	dot_product(a, b):
	return sum(x*y for x, y in zip(a, b))

# ============== ~ MATRICES OPERATIONS ~ ============== #

def add_matrices(a, b):
	result = create_matrix(len(a), len(a[0]))
	for i in range (len(a)):
		for j in range (len(a[0])):
			result[i][j] = a[i][j] + b[i][j]
	return result
	
def sub_matrices(a, b):
	result = create_matrix(len(a), len(a[0]))
	for i in range (len(a)):
		for j in range (len(a[0])):
			result[i][j] = a[i][j] - b[i][j]
	return result

def div_matrix_scalar(a, b):
	result = create_matrix(len(a), len(a[0]))
	for i in range (len(a)):
		for j in range (len(a[0])):
			result[i][j] = a[i][j] / b
	return result

def mul_matrix_scalar(a, b):
	result = create_matrix(len(a), len(a[0]))
	for i in range (len(a)):
		for j in range (len(a[0])):
			result[i][j] = a[i][j] * b
	return result

def mul_matrices(a, b):
	result = create_matrix(len(a), len(b[0]))
	for i in range (len(a)):
		for j in range(len(b[0])):
			result[i][j] = dot_product(a[i], align_row(b, j))
	return (result)

# ============== ~ MATRIX ~ ============== #

class Matrix:
	def __init__(self, input):
		assert isinstance(input, tuple) or isinstance(input, list)
		if (isinstance(input, tuple)):
			assert len(input) == 2
			assert isinstance(input[0], int) and isinstance(input[1], int)
			self.shape = input
			self.data = create_matrix(input[0], input[1])
		elif (isinstance(input, list)):
			for lst in input:
				assert len(input[0]) == len(lst)
				for lst_elem in lst:
					assert isinstance(lst_elem, float)
			self.shape = (len(input), len(input[0]))
			self.data = input

	def __add__(self, other):
		assert isinstance(other, type(self))
		assert self.shape == other.shape
		return Matrix(add_matrices(self.data, other.data))
	
	__radd__ = __add__
	
	def __sub__(self, other):
		assert isinstance(other, type(self))
		assert self.shape == other.shape
		return Matrix(sub_matrices(self.data, other.data))

	def __rsub__(self, other):
		assert isinstance(other, type(self))
		assert self.shape == other.shape
		return Matrix(sub_matrices(other.data, self.data))

	def __truediv__(self, other):
		assert isinstance(other, int) or isinstance(other, float)
		return Matrix(div_matrix_scalar(self.data, other))

	__rtruediv__ = __truediv__

	def __mul__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return Matrix(mul_matrix_scalar(self.data, other))
		elif isinstance(other, type(self)):
			assert self.shape[1] == other.shape[0] 
			return (Matrix(mul_matrices(self.data, other.data)))
	
	def T(self):
		self.shape = (self.shape[1], self.shape[0])
		self.data = [list(row) for row in (zip(*self.data))]
		return self

truc = Matrix([[1.0, 2.0, 3.0],[4.0, 5.0, 6.0]])
truc2 = Matrix([[7.0, 8.0], [9.0, 10.0], [11.0, 12.0]])

m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
[0.0, 2.0, 4.0, 6.0]])

m2 = Matrix([[0.0, 1.0],
[2.0, 3.0],
[4.0, 5.0],
[6.0, 7.0]])

m3 = Matrix([[0.0,1.0], [2.0,3.0], [4.0,5.0]])
m4 = Matrix([[0.0,1.0], [2.0,3.0], [4.0,5.0]])
result = m3 * 2
print(result.data, result.shape)
# print(truc.data, truc.shape)
# print (Matrix((2, 3)).data)