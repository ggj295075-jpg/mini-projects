import numpy as np

# Cosine Similarity Func
def cosine_similarity(X):
    dot = np.dot(X,X.T)
    norms = np.linalg.norm(X,axis=1)
    norms_matrix = np.outer(norms, norms)
    similarity = dot / np.maximum(norms_matrix, 1e-10)
    similarity = np.clip(similarity, -1, 1)
    return similarity
# Euclidean Distance Func
def piarwise_distance(X):
    sq_sum = np.sum(np.square(X), axis=1, keepdims=True)
    sq_distance = sq_sum + sq_sum.T
    sq_distance = sq_distance - 2 * np.dot(X, X.T)
    sq_distance = np.maximum(sq_distance, 0)
    return np.sqrt(sq_distance)

a = np.array([[1,3,4,4], [4,2,6,9,]])

print(piarwise_distance(a))
print(cosine_similarity(a))

# I'll finish write it later
