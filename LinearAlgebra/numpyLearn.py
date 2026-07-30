import numpy as np
import math


vectorA = np.array([1, 2, 3, 4])
vectorB = np.array([3, 2, 1])
Result = vectorA * vectorB[:, np.newaxis]
print("Broadcast:\n", Result)
print("Shape:\n", Result.shape)

# Cut vectors and matrix:
print("VectorA:\n",vectorA)
print("VectorB:\n", vectorB)


