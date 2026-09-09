import numpy as np

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

print("MatrixA:\n", matrixA)
print("MatrixB:\n", matrixB)

