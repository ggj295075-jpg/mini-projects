from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine

data = load_wine()

X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, test_size=0.2
)

dtc = DecisionTreeClassifier(max_depth=5)
model = BaggingClassifier(
    estimator=DecisionTreeClassifier(), n_estimators=100, random_state=42
)
dtc.fit(X_train, y_train)
model.fit(X_train, y_train)

print(dtc.score(X_test, y_test))
print(model.score(X_test, y_test))
