import numpy as np

matrix = np.array([[1,3,4,5], [4,6,3,1], [0,2,7,1]])

U, S, Vt = np.linalg.svd(matrix, full_matrices=False)

print("U: ", U)
print("S: ", S)
print("Vt: ", Vt)
