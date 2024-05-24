import numpy as np
import matplotlib.pyplot as plt

def logistic_map(b, x0, num_iterations):
    x = x0
    for _ in range(num_iterations):
        x = b * x * (1 - x)
    return x

b_values = np.arange(2.5, 3.51, 0.01)
x0 = 0.5  # Initial condition
num_iterations = 1000  # Number of iterations to reach steady state
num_last_points = 100  # Number of points to collect after reaching steady state

converged_points = {}

for b in b_values:
    x = x0
    for _ in range(num_iterations):
        x = b * x * (1 - x)
    
    # Collect the last num_last_points to check for convergence
    last_points = []
    for _ in range(num_last_points):
        x = b * x * (1 - x)
        last_points.append(x)
    
    # Remove duplicates to find unique points (convergence or periodic points)
    unique_points = np.unique(np.round(last_points, decimals=6))
    converged_points[b] = unique_points

# Plotting the bifurcation diagram
plt.figure(figsize=(10, 7))
for b, points in converged_points.items():
    plt.plot([b] * len(points), points, 'k.', markersize=2)

plt.title("Bifurcation diagram of the logistic map")
plt.xlabel("b")
plt.ylabel("x")
plt.grid(True)
plt.show()
