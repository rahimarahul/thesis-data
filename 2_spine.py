import numpy as np
import plotly.graph_objects as go



# Parameter t from -π to π
t = np.linspace(-np.pi, np.pi, 2000)

# -------------------------
# S-curve #1 (lower)
# -------------------------
x1 = np.sin(t)
y1 = t
z1 = np.cos(t)

# Add thickness (scatter cloud)
noise = 0.05
x1_cloud = x1 + np.random.normal(0, noise, len(t))
y1_cloud = y1 + np.random.normal(0, noise, len(t))
z1_cloud = z1 + np.random.normal(0, noise, len(t))

# -------------------------
# S-curve #2 (upper, mirrored + shifted)
# -------------------------
x2 = -np.sin(t)  # mirrored horizontally
y2 = t
z2 = np.cos(t) + 2  # lifted upward

# Add cloud for curve #2
x2_cloud = x2 + np.random.normal(0, noise, len(t))
y2_cloud = y2 + np.random.normal(0, noise, len(t))
z2_cloud = z2 + np.random.normal(0, noise, len(t))

# -------------------------
# Plotly 3D figure
# -------------------------
fig = go.Figure()

# Curve 1 cloud
fig.add_trace(go.Scatter3d(
    x=x1_cloud, y=y1_cloud, z=z1_cloud,
    mode="markers",
    marker=dict(size=2, color="lightblue"),
    name="S-curve 1 cloud"
))

# Curve 2 cloud
fig.add_trace(go.Scatter3d(
    x=x2_cloud, y=y2_cloud, z=z2_cloud,
    mode="markers",
    marker=dict(size=2, color="pink"),
    name="S-curve 2 cloud"
))
# Extra in-between points
extra_points = np.array([[0, 3, 0],[0, 0, 1.5],[0, -3, 0]])
fig.add_trace(go.Scatter3d(
    x=extra_points[:, 0],
    y=extra_points[:, 1],
    z=extra_points[:, 2],
    mode='markers+text',
    text=['IB'] * len(extra_points),
    textposition='top center',
    name='In-between points',
    marker=dict(
        size=8,
        color='green',
        line=dict(color='black', width=1)
    )
))

# Layout
fig.update_layout(
    title="3D DOUBLE S-Curve (Mirrored + Lifted)",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Z",
        aspectmode="cube"
    ),
    width=900,
    height=900
)


fig.show()
