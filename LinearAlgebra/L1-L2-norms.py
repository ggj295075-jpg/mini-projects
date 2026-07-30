import numpy as np
import math

vectorA = np.array([1,2,3,4])

# L1 and L2 norms:
sum = 0 # L1
for i in vectorA:
    sum += abs(i)
print(f"L1: {sum}")

sqrt_sum = 0 # L2
for i in vectorA:
    sqrt_sum += math.sqrt(abs(i))
print(f"L2: {sqrt_sum}")

