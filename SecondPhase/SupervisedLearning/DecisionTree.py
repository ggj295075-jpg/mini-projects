from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import (
    DecisionTreeRegressor,
)  # Therefore it type of DecisionTree doensn't need, I don't use it
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

data = load_wine()

X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, test_size=0.2
)

dtc = DecisionTreeClassifier(max_depth=3, random_state=42)
dtc.fit(X_train, y_train)
print(dtc.score(X_test, y_test))
