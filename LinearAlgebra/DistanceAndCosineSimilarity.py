import numpy as np

# L1 and L2 distance:
def EuclidDist(array1, array2): # L2-distance func
    return np.sqrt(np.sum((array1 - array2)**2)) # np.linalg.norm(array1, array2)
def ManhattanDist(array1, array2): # L1-distance func
    return np.sum(np.abs(array1 - array2))
# Cosine Similarity:
def CosineSimilarity(array1, array2):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b)) # or a@b


a = np.array([1,2,3,4])
b = np.array([4,3,2,1])

print("Euclidean Distance(L1-distance): ", EuclidDist(a, b))
print("Manhattan Distance(L1-distance): ", ManhattanDist(a, b))
print("CosineSimilarity: ", CosineSimilarity(a,b))
print("VectorA: ", a)
print("VectorB: ", b)

