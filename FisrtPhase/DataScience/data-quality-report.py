import numpy as np

def myfucn(list):
    "Return GOOD if obj in list > 10 and < 100. Else return BAD"
    if list > 10 and list < 100:
        return "GOOD"
    else:
        return "BAD"

sort = np.vectorize(myfucn)

li = np.array([1,2,2,3,4,5,6,100,11, 59, 33, 99, 101])
print(sort(li))
print(f"\"{sort.__doc__}\"")

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix[[0, 2], [1,2]])