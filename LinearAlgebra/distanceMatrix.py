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



def find_top_k_items(X, mode:str):
    space_matrix = [] # create empty matrix
    for i in range(len(X)):
        row = [round(float(X[i][j]), 3) for j in range(len(X)) if i != j] # collect objects from vector in matrix
        if mode == "distance":
            row.sort()
            vals = row[:3]
        elif "similarity":
            row.sort(reverse=True)
            vals = row[:3]
        else:
            raise ValueError("mode must be \"similarity\" or \"distance\".")
        while len(vals) < 3: # if obj in vector less 3 add zeros
            vals.append(0.0)
        space_matrix.append(vals)
    return space_matrix
a = np.array([[1,3,4,4], [4,2,6,9,], [8,2,1,3], [3,2,9,1]])

print("Eucliden distance:\n",piarwise_distance(a))
print("Cosine Similarity:\n",cosine_similarity(a))

pire = piarwise_distance(a)
cosine = cosine_similarity(a)
# Distance matrixs:
print("\n\nDistance matrix of Eullidean matrix: ", find_top_k_items(pire, "distance"), "\n\n")
print("Distance matrix of CosimeSimilarity matrix: ", find_top_k_items(cosine, "similarity"))
