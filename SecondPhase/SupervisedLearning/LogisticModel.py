from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


X, y = load_breast_cancer(return_X_y=True) # Load binary-dataset from sklearn
scaler = StandardScaler() # Initialization scaler for set dataset values necessary size
X_scaler = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaler, y, test_size=0.2, random_state=42) # Divide dataset to train part and test part

logreg = LogisticRegression(max_iter=1000, C=0.05, solver='liblinear') # This set of parameters give the biggest score
logreg.fit(X_train, y_train)
print(logreg.predict(X_test))
print(logreg.score(X_test, y_test))
print(logreg.score(X_test, y_test)) # Display a % of a right responses of model
print(logreg.coef_) # Display a weights
print(logreg.intercept_) # Display a bias
