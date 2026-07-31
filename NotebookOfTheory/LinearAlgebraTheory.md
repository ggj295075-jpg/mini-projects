# It is note with Theory of step 0.1 in ml-engineer plan[/home/alo/Documents/ml-llm-roadmap.md].
- A vector is an array (set of data types). It may have a few arrays.Example:
  - vectorA = ([1, 2, 3, 4])
  - vectorB = (["one", "two", "three", "four"])

- A matrix is a set of data types. He ranged of horizontal rows and vertical columns. Example:
[1, 2, 3, 4,
5, 6, 7, 8
9, 0, 1, 2]

- A tensor is a set of data types. He is have 3+ parameters of range. Example: 
[[1,2,3,4], [1,2,3,4]
[1,2,3,4], [1,2,3,4]]

- *Broadcast in numpy - multiple. 

- *Shape in numpy. Returns (n,) in array, (columns, rows) in vector, (rows, columns, arrays) in tensor.

# Scalar and Matrix multiple: 

 The scalar multiple is a multiple of first num in vector and first num in another vector + multiple of first num in vector and second num in another vector...
- Example: $vectorA = [10, 5]$   $vectorB = [-1, 3]$. They scalar = $10*(-1) + 5*3 = -10 + 15 = 5$

 The matrix multiple is a muptiple of every num in a first row in matrix to every num in first column in another matrix, etc. But there is restriction: an amount nums in rows must be equal to amount nums in columns an another matrix. Example:
$$matrix_{a} = \begin{pmatrix} 1 & 2 & 3 & \\ 4 & 5 & 6\end{pmatrix}$$ * $$matrix_{b} = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$$ = $$matrix_(a*b) = \begin{pmatrix} 14 & 32 \\ 32 & 77 \end{pmatrix}$$

- Operations: 1num = 1 row * 1 colum, 2num = 1row * 2 column, 3num = 2 row * 1 column, 4num = 2 row * 2 column


# Rank, Basis, Projection:

A rank is a max amount a linear independent columns (or rows). This is a dimension linear columns.

A basis is a set of vectors ${v_{1}, \cdots, v_{n} }$. 
   - Dimension = an amount vectors in a basis.
   - Default basis $R^3$: $e_{1} = (1,0,0), e_{2} = (0,1,0), e_{3} = (0,0,1)$


# L1 and L2 norms:

Norms:
  - This is way to measure "len" of vector.

L1:
  - It is a sum of values in vector. Example: [3, -4] = |3| + |-4| = 3 + 4 = 7.

L2:
  - It is a square root of $values^2$ in vector. Example [3, -4] = $\sqrt{3^2 + 4^2}$ = 5


# Distance:

  - Euclidean distance(L2-distance): It is $\sqrt{(a_{1} - b_{1})^2 + (a_{2} - b_{2})^2 + \cdots}$ . Distance of dots in space.

  - Manhattan distance(L1-distance): It is $|a_{1} - b_{1}| + |a_{2} - b_{2}| + \cdots$ . How much a steps between dots.

# Cosine similarity:

  - Formula: $\frac{a*b}{||a||_{2} * ||b||_{2}}$
  If result = 1 - vectors in one direction. 0 - a vectors is perpedicular. -1 - a vectors is opposite.


# Eigenvectors and eigenvalues:
  - Eigenvectors it is the not zero vector, which doesn't change direction when matrix multiply. But change his len.
  - eigenvalue it is a value, which show by how many times changing tensile force. $$\alpha$$
