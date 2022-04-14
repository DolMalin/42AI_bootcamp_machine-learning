from matrix import Matrix, Vector

# Should print a 2x2 matrix filled with 0
A = Matrix((2,2))
print(A)
print("")

# Should print a 2x2 and a 2x3 matrices, then their transposes
A = Matrix([[2.0, 4.0], [6.0, 8.0]])
B = Matrix([[2.0, 2.0, 2.0], [2.0, 2.0, 2.0]])
print(A)
print(B)
print(A.T())
print(B.T())
print("")

# A + B should print an error because the shapes aren't the same
A = Matrix([[2.0, 4.0], [6.0, 8.0]])
B = Matrix([[2.0, 2.0, 2.0], [2.0, 2.0, 2.0]])
# A + B

# A + B should print a 2x2 matrice of [[4.0, 6.0],[8.0, 10.0]]
A = Matrix([[2.0, 4.0], [6.0, 8.0]])
B = Matrix([[2.0, 2.0], [2.0, 2.0]])
print(A+B)
print("")

# A + 2 should print an error because you can't add a scalar
# print(A+2)

# A - B should print a 2x2 matrix of [[0.0, 2.0],[4.0, 6.0]]
print(A-B)
print("")

# A - 2 should print an error because you can't substract by scalar
# print(A-2)

# A * B should print an error because the shapes doest fit(B must have as much rows as A have columns)
A = Matrix([[2.0, 3.0, 4.0], [5.0, 6.0, 8.0]])
B = Matrix([[2.0, 2.0], [2.0, 2.0]])
# print(A*B)

# B * A should print a 2x3 matrix
print(B*A)
print("")


