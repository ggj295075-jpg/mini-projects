import numpy as np
import math

matrix = np.array([[1,2], [0, 3], [3, 0]])

num_point = len(matrix)

space_matrix = [[0.0] * num_point for _ in range(num_point)]

for i in range(num_point):
    for j in range(num_point):
        p1 = matrix[i]
        p2 = matrix[j]

        euclid_dist_x = (p1[0]-p2[0])**2
        euclid_dist_y = (p1[1]-p2[1])**2

        distance = math.sqrt(euclid_dist_x + euclid_dist_y)
        space_matrix[i][j] = distance

print(space_matrix)

