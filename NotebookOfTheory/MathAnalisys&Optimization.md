# It is a theory note of Phase 0.2 in my ml roadmap.

> [!NOTE]
> *First I'll write will be derivative.*

**Derivative measure a changes speed of function.**
  - We use to the derivative for:
    - gradient descent
    - loss function
    - backpropagation

*Partial Derivative - is the derivative of a function of a few variable with a one variable.*
  - We use to the partial derivative for:
    - gradient descent
    - multivariate loss function
    - gradient

> [!NOTE]
> Gradient Descent:
  - Formula: $$W_{new} = W_{old} - a * \frac{dL}{dW}$$
  - L - loss
  - W - a single specific weight
  - a - a speed of train

> [!NOTE]
> Jacobian and Hessian Matrix:
  - Jacobian matrix - it is a matrix everyone of partial derivative vector function.
$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
$$

