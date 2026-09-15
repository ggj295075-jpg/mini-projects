from sklearn import linear_model
import numpy as np

X = np.array([[10, 0, 2, 1],
              [35, 1, 7, 0.3],
              [65, 1, 20, 0.1]])


reg = linear_model.LinearRegression()

reg.fit(X, [2000, 6000, 10000])
print(reg.coef_)
print(reg.intercept_)
print(reg.predict([[13.5, 1, 3, 0.1],
              [20, 0, 5, 0.7],
              [100, 1, 30, 1]]))

