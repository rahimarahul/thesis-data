import numpy as np
import plotly.graph_objects as go
from sklearn.datasets import make_moons

# Create the S-shape (two half circles)
X, y = make_moons(n_samples=4000, noise=0.05, random_state=42)

# Separate the two halves
upper = X[y == 0]
lower = X[y == 1]

# Extra points
extra_points = np.array([
    [0.5, 0.2],
    [-0.5, 0],
    [1.47, 0.4]
])

# Create smooth z-values from 0 to 1
z_upper = np.linspace(0, 1, len(upper))
z_lower = np.linspace(0, 1, len(lower))

# Extra points at mid z = 0.5
z_extra = np.ones(len(extra_points)) * 0.5

# Create 3D figure
fig = go.Figure()

# Upper half circle
fig.add_trace(go.Scatter3d(
    x=upper[:, 0], y=upper[:, 1], z=z_upper,
    mode='markers',
    marker=dict(size=2, color='blue'),
    name='Upper half circle (z=0→1)'
))

# Lower half circle
fig.add_trace(go.Scatter3d(
    x=lower[:, 0], y=lower[:, 1], z=z_lower,
    mode='markers',
    marker=dict(size=2, color='red'),
    name='Lower half circle (z=0→1)'
))

# Extra points
fig.add_trace(go.Scatter3d(
    x=extra_points[:, 0], y=extra_points[:, 1], z=z_extra,
    mode='markers',
    marker=dict(size=6, color='green', line=dict(color='black', width=2)),
    name='In-between points (z=0.5)'
))

# Layout
fig.update_layout(
    title="3D make_moons with Smooth z from 0 → 1",
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectmode='data'
    ),
    width=750,
    height=750
)

fig.show()