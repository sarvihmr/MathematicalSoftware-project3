import numpy as np
from scipy.integrate import trapezoid, simpson, quad

f = lambda x: np.exp(x**2)
a, b = 0, 1
n = 100

x = np.linspace(a, b, n + 1)
y = f(x)

trap_res = trapezoid(y, x)

simp_res = simpson(y, x)

gauss_res, _ = quad(f, a, b)

print(f"Trapezoid Method: {trap_res:.8f}")
print(f"Simpson Method:   {simp_res:.8f}")
print(f"Gaussian Method:  {gauss_res:.8f}")
print(f"Trapezoid Error:  {abs(trap_res - gauss_res):.2e}")
print(f"Simpson Error:    {abs(simp_res - gauss_res):.2e}")