from numpy import dot, sum

y = dot(X, w) + b
cost = sum((y - t) ** 2 / (2.0 * N))
