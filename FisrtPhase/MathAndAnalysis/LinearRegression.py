import numpy as np

X = np.array([100, 250, 400, 500, 1000])
y = np.array([50, 125, 200, 250, 500])

X = (X - X.mean()) / X.std()

w = 0.0
b = 0.0
a = 0.08
epochs = 100

m = len(y)

for epoch in range(epochs):
    y_pred = w * X + b

    loss = np.mean((y_pred - y) ** 2)

    dw = (2/m) * np.sum((y_pred - y) * X)
    db = (2/m) * np.sum(y_pred - y)

    w = w - a * dw
    b = b - a * db

    if epoch % 20 == 0:
        print(f"epoch: {epoch}, loss={loss:.2f}, w={w:.3f}, b={b:.2f}")

print("W", w)
print("B", b)
