# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdal-mol <dolmalinn@gmail.com>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/12 10:54:32 by pdal-mol          #+#    #+#              #
#    Updated: 2022/04/12 14:40:47 by pdal-mol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Matrix:
	def __init__(self, input):
		assert isinstance(input, tuple) or isinstance(input, list)
		if (isinstance(input, tuple)):
			assert len(input) == 2
			assert isinstance(input[0], int) and isinstance(input[1], int)
			self.shape = input
			self.data = [[0.0] * input[1]] * input[0]
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
		result = self.data
		for i in range (len(self.data)):
			for j in range (self.shape[1]):
				result[i][j] = self.data[i][j] + other.data[i][j]
		return Matrix(result)
	
	__radd__ = __add__

			
	def T(self):
		self.shape = (self.shape[1], self.shape[0])
		self.data = [list(row) for row in (zip(*self.data))]
		return self

	
		
	
			
truc = Matrix([[1.0, 5.0],[-4.0, 3.0]])
truc2 = Matrix([[2.0, -1.0], [4.0, -1.0]])

result = truc + truc2
# print(truc.data, truc.shape)
print (result.data)