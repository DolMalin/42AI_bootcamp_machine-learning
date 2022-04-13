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

def create_matrix(row, col):
	return [[0.0 for x in range(col)] for y in range(row)]


def col_to_row(matrix, row):
	return [matrix[x][row] for x in range(len(matrix))]


def dot_product(a, b):
	return sum(x*y for x, y in zip(a, b))


# ============== ~ MATRICES OPERATIONS ~ ============== #

def add_matrices(a, b):
	result = create_matrix(len(a), len(a[0]))
	for i in range(len(a)):
		for j in range(len(a[0])):
			result[i][j] = a[i][j] + b[i][j]
	return result


def add_vectors(a, b):
	if a.shape == b.shape:
		result = create_matrix(len(a), len(a[0]))
		for i in range(len(a)):
			for j in range(len(a[0])):
				result[i][j] = a[i][j] + b[i][j]
		return result


def sub_matrices(a, b):
	result = create_matrix(len(a), len(a[0]))
	for i in range(len(a)):
		for j in range(len(a[0])):
			result[i][j] = a[i][j] - b[i][j]
	return result


def div_matrix_scalar(a, b):
	result = create_matrix(len(a), len(a[0]))
	for i in range(len(a)):
		for j in range(len(a[0])):
			result[i][j] = a[i][j] / b
	return result


def mul_matrix_scalar(a, b):
	result = create_matrix(len(a), len(a[0]))
	for i in range(len(a)):
		for j in range(len(a[0])):
			result[i][j] = a[i][j] * b
	return result


def mul_matrix_vector(a, b):
	if len(b) > 1:
		result = create_matrix(len(a), len(b[0]))
		for i in range(len(a)):
			sum = 0
			for j in range(len(b)):
				sum += a[i][j] * b[j][0]
			result[i][0] = sum
		return result
	else:
		result = create_matrix(len(a), len(b))
		for i in range(len(a)):
			sum = 0
			for j in range(len(b[0])):
				sum += a[i][j] * b[0][j]
			result[i][0] = sum
		return result


def mul_matrices(a, b):
	result = create_matrix(len(a), len(b[0]))
	for i in range(len(a)):
		for j in range(len(b[0])):
			result[i][j] = dot_product(a[i], col_to_row(b, j))
	return (result)


def mul_vectors(a, b):
	v1 = [col_to_row(a, 0)] if len(a) > 1 else a
	v2 = [col_to_row(b, 0)] if len(b) > 1 else a
	return (dot_product(v1[0], v2[0]))


# ============== ~ CLASSES ~ ============== #


class Matrix:
	def __init__(self, input):
		assert type(input) == tuple or type(input) == list
		if (type(input) == tuple):
			assert len(input) == 2
			assert type(input[0]) == int and type(input[1]) == int
			self.shape = input
			self.data = create_matrix(input[0], input[1])
		else:
			for lst in input:
				assert len(input[0]) == len(lst)
				for lst_elem in lst:
					assert type(lst_elem) == float
			self.shape = (len(input), len(input[0]))
			self.data = input

	def __add__(self, other):
		if type(self) == Matrix and type(other) == Matrix:
			assert self.shape == other.shape
			return Matrix(add_matrices(self.data, other.data))
		elif type(self) == Vector and type(other) == Vector:
			return Vector(add_matrices(self.data, other.data))

	__radd__ = __add__

	def __sub__(self, other):
		assert type(other) == type(self) and self.shape == other.shape
		return Matrix(sub_matrices(self.data, other.data))

	def __rsub__(self, other):
		assert type(other) == type(self) and self.shape == other.shape
		return Matrix(sub_matrices(other.data, self.data))

	def __truediv__(self, other):
		assert type(other) == int or type(other) == float
		return Matrix(div_matrix_scalar(self.data, other))

	__rtruediv__ = __truediv__

	def __mul__(self, other):
		if type(other) == int or type(other) == float:
			return Matrix(mul_matrix_scalar(self.data, other))
		elif type(other) == Matrix and type(self) == Matrix:
			assert self.shape[1] == other.shape[0]
			return (Matrix(mul_matrices(self.data, other.data)))
		elif type(self) == Matrix and type(other) == Vector:
			return (Matrix(mul_matrix_vector(self.data, other.data)))

	__rmul__ = __mul__

	def __str__(self):
		return '<Matrix (shape=' + str(self.shape) + ', data=' + str(self.data) + ')'

	__repr__ = __str__

	def T(self):
		return Matrix([list(row) for row in (zip(*self.data))])


class Vector(Matrix):
	def __init__(self, input):
		assert isinstance(input, list)
		if len(input) > 1:
			for i in range(len(input)):
				assert len(input[i]) == 1
			self.data = input
			self.shape = (len(input), 1)
		elif (len(input) == 1):
			assert len(input[0]) > 1 and len(input[0]) < 4
			self.data = input
			self.shape = (1, len(input[0]))

	def dot(self, other):
		assert type(other) == Vector
		return mul_vectors(self.data, other.data)
