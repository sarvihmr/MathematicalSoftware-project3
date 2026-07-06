import numpy as np
import sympy as sp
from scipy.interpolate import lagrange, CubicSpline

x = np.array([1, 2, 3, 4, 5, 6], dtype=float)
y = np.array([1, 3, 5, 8, 5, 2], dtype=float)

# Lagrange
poly = lagrange(x, y)

X = sp.Symbol('x')
expr = sum(sp.Float(c) * X**i for i, c in enumerate(poly.coef[::-1]))
expr = sp.expand(expr)


print("Lagrange Polynomial:\n")
print(sp.N(expr, 10))
print("\n" + "=" * 60 + "\n")

# Cubic Spline
cs = CubicSpline(x, y)

X = sp.Symbol('x')

print("Spline interpolation:\n")

for i in range(len(x)-1):
    a, b, c, d = cs.c[:, i]
    formula = a*(X-x[i])**3 + b*(X-x[i])**2 + c*(X-x[i]) + d
    formula = sp.expand(formula)

    print(f"{x[i]} <= x <= {x[i+1]}")
    print(sp.N(formula, 10))
    print()