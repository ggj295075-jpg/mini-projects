import numpy as np


vectorA = np.array([1, 2, 3, 4])
vectorB = np.array([3, 2, 1])
Result = vectorA * vectorB[:, np.newaxis]
print("Broadcast:\n", Result)
print("Shape:\n", Result.shape)

# Element-wise and matrix multiplication
matrixA = np.array([[1,2,3,4],
                   [5,6,7,8]])
matrixB = np.array([[1,2],
                   [3,4],
                   [5,6],
                   [7,8]])
element_wise_result = matrixA * matrixA # or np.multiply(matrixA, matrixA)
matrix_result = matrixA @ matrixB # or np.matmul(matrixA, matrixB)
print("Element-wise multiplication(matrixA*matrixA):\n", element_wise_result)
print("Matrix multiplication(matrixA*matrixB):\n", matrix_result)
print("Matrix multiplication(matrixB*matrixA:\n", matrixB @ matrixA)

# Cut vectors and matrix:
print("VectorA:\n",vectorA)
print("VectorB:\n", vectorB)
print("MatrixA:\n", matrixA)
print("MatrixB:\n", matrixB)
