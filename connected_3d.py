import numpy as np
import plotly.graph_objects as go
from sklearn.datasets import make_circles
import common_utils

# Generate a base circle dataset (concentric)
X, y = make_circles(n_samples=5000, noise=0.02, factor=0.7, random_state=42)

# Separate the two circles
circle1 = X[y == 0]   # inner circle
circle2 = X[y == 1]   # outer circle

# Shift one circle to make them intersect in XY
shift = np.array([0.7, 0])
circle2_shifted = circle2 + shift

# Extra points
extra_points = np.array([
    [0.5, 0],
    [-0.5, 0]
])

# Assign z-levels
z1 = np.zeros(len(circle1))          # Circle 1 at z = 0
z2 = np.ones(len(circle2_shifted))   # Circle 2 at z = 1
z_extra = np.ones(len(extra_points)) * 0.5  # Mid-level points at z = 0.5

circle1_3d = np.column_stack((circle1, z1))
circle2_3d = np.column_stack((circle2_shifted, z2))

#fig = common_utils.create_3d_figure(circle1_3d, circle2_3d ,extra_points)

# Create a 3D Plotly figure
fig = go.Figure()

# Circle 1 (z = 0)
fig.add_trace(go.Scatter3d(
    x=circle1_3d[:,0], y=circle1_3d[:,1], z=circle1_3d[:,2],
    mode='markers',
    marker=dict(size=2, color='blue'),
    name='Circle 1 (z=0)'
))

# Circle 2 (z = 1)
fig.add_trace(go.Scatter3d(
    x=circle2_3d[:,0], y=circle2_3d [:,1], z=circle2_3d[:,2],
    mode='markers',
    marker=dict(size=2, color='red'),
    name='Circle 2 (z=1)'
))

# Extra points in between (z = 0.5)
fig.add_trace(go.Scatter3d(
    x=extra_points[:,0], y=extra_points[:,1], z=z_extra,
    mode='markers',
    marker=dict(size=6, color='green', line=dict(width=2, color='black')),
    name='In-between Points (z=0.5)'
))

fig.update_layout(
    title="Two Intersecting Circles at Different Z-Levels (Plotly 3D)",
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