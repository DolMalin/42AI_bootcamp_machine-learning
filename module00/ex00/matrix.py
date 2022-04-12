# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdal-mol <dolmalinn@gmail.com>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/12 10:54:32 by pdal-mol          #+#    #+#              #
#    Updated: 2022/04/12 12:28:27 by pdal-mol         ###   ########.fr        #
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
			
	def T(self):
		self.shape = (self.shape[1], self.shape[0])
		return self
		

			
truc = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
print(truc.data, truc.shape)

print(truc.T().shape)