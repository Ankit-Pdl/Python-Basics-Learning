import numpy as np

# Regression Problem
x = np.array([2, 4, 6, 8, 10])
y = np.array([1.4, 2.0, 2.4, 2.6, 2.8])

n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x2 = np.sum(x**2)
sum_x3 = np.sum(x**3)
sum_x4 = np.sum(x**4)
sum_xy = np.sum(x*y)
sum_x2y = np.sum(x**2 * y)

A_reg = np.array([
    [n, sum_x, sum_x2],
    [sum_x, sum_x2, sum_x3],
    [sum_x2, sum_x3, sum_x4]
])
B_reg = np.array([sum_y, sum_xy, sum_x2y])

coeffs = np.linalg.solve(A_reg, B_reg)
print(f"Regression sums: sum_x={sum_x}, sum_y={sum_y}, sum_x2={sum_x2}, sum_x3={sum_x3}, sum_x4={sum_x4}, sum_xy={sum_xy}, sum_x2y={sum_x2y}")
print(f"Regression Coeffs: a={coeffs[0]:.2f}, b={coeffs[1]:.2f}, c={coeffs[2]:.2f}")

# Jacobi Iteration Problem
def jacobi_step(x, y, z):
    new_x = (14 - y - 3*z) / 5
    new_y = (7 - x - 9*z) / 10
    new_z = (17 + 2*x - 7*y) / 10
    return new_x, new_y, new_z

x_j, y_j, z_j = 0.0, 0.0, 0.0
print("\nJacobi Iterations:")
for i in range(1, 11):
    x_j, y_j, z_j = jacobi_step(x_j, y_j, z_j)
    print(f"Iteration {i}: x={x_j:.2f}, y={y_j:.2f}, z={z_j:.2f}")

# Cubic Spline f(2)
f2 = 0.25*(2-1)**3 + 0.75*(3-2) + 1.25*(2-1)
print(f"\nCubic Spline f(2) = {f2:.2f}")