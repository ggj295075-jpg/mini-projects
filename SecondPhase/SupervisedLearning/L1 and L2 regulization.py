from sklearn import linear_model
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
import pandas as pd


l1 = linear_model.Lasso(alpha=0.05)
l2 = linear_model.Ridge(alpha=0.05)

X,y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

l1.fit(X_train, y_train)
l2.fit(X_train, y_train)
print(f"Score L1: {l1.score(X_test, y_test)}")
print("Coef: ", l1.coef_, "Intercept: ",l1.intercept_)
print(f"Score L2: {l2.score(X_test, y_test)}")
print("Coef: ", l2.coef_, "Intercept: ", l2.intercept_)

print("-" * 50)
linreg = linear_model.LinearRegression()

df = pd.read_csv("housing.csv")
X = df.drop(columns=["MEDV"])
y = df["MEDV"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
linreg.fit(X_train, y_train)
print(f"Score Linear Regression: l" ,linreg.score(X_test, y_test))
print(f"Coef: {linreg.coef_} Intercept: {linreg.intercept_}")