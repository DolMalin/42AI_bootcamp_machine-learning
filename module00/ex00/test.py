
def	create_matrix(row, col):
	return [[0.0 for x in range (col)] for y in range (row)]

def add_matrices(a, b):
	result = create_matrix(len(a), len(a[0]))
	print(result)
	for i in range (len(a)):
		for j in range (len(a[0])):
			result[i][j] = a[i][j] + b[i][j]
	return result


def	align_row(matrix, row):
	return [matrix[x][row] for x in range(len(matrix))]

def	dot_product(a, b):
	return sum(x*y for x, y in zip(a, b))

def mul_matrices(a, b):
	result = create_matrix(len(a), len(b[0]))
	for i in range (len(a)):
		for j in range(len(b[0])):
			result[i][j] = dot_product(a[i], align_row(b, j))
	return (result)

# assert self.shape[1] == other.shape[0] 
# result = create_matrix(self.shape[0], other.shape[1])
# for i in range (self.shape[0]):
# 	for j in range(other.shape[1]):
# 		row = self.data[i]
# 		col = [other.data[x][j] for x in range(len(other.data))]
# 		result[i][j] = sum(x*y for x, y in zip(row, col)) 

m1 = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
m2 = [[7.0, 8.0], [9.0, 10.0], [11.0, 12.0]]
print(mul_matrices(m1, m2))