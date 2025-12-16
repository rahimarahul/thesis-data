import numpy as np
from sklearn.datasets import make_circles
import common_utils
import plotly.graph_objects as go

# ---- Create 2D concentric circles ----
X, y = make_circles(
    n_samples=5000,   # total number of points
    factor=0.5,       # inner circle relative size
    noise=0.05,       # add noise for realism
    random_state=42
)

# ---- Convert to 3D ----
# Add a third dimension (z = small random noise, or zeros)
z = np.random.normal(0, 0.5, size=X.shape[0])  # small height variation
X_3d = np.column_stack((X, z))

# ---- Define extra 3D points ----
extra_points = np.array([
    [0, -0.75, -0.5],
    [0.8, 0, 0],
[0, 0.75, 0.5]
])
fig = common_utils.create_3d_figure(X_3d, y, extra_points)