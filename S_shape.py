import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons

# Create two half circles (the "S" shape)
X, y = make_moons(n_samples=4000, noise=0.05, random_state=42)

# Plot
plt.figure(figsize=(6,6))
plt.scatter(X[y==0, 0], X[y==0, 1], color='blue', label='Upper half circle')
plt.scatter(X[y==1, 0], X[y==1, 1], color='red', label='Lower half circle')
plt.axis('equal')
plt.title("Two Half Circles (S-shape) using sklearn.make_moons")
plt.legend()
#Extra points
extra_points = np.array([
[0.5, 0.2],
[-0.5, 0],
[1.47, 0.4]
])
# Plot all extra points at once (single legend entry)

plt.scatter(
extra_points[:, 0],
extra_points[:, 1],
c="green",
s=50,
edgecolor="black",
label="In-between points"
)
plt.show()