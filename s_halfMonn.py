from sklearn.datasets import make_s_curve, make_moons
import numpy as np
import plotly.graph_objects as go

# --- 3D S-curve ---
n_s = 5000
X_s, t_s = make_s_curve(n_samples=n_s, noise=0.05, random_state=42)

# --- 2D Half Moons ---
n_m = 2000
X_m, y_m = make_moons(n_samples=n_m, noise=0.05, random_state=42)

# Separate upper and lower moons
upper = X_m[y_m == 0]
lower = X_m[y_m == 1]

# Map z from 0 to 1 for each half moon
z_upper = np.linspace(0, 1, len(upper))
z_lower = np.linspace(0, 1, len(lower))

# Optionally scale x/y to match S-curve range
scale = 2.5
upper_3d = np.c_[upper[:,0]*scale, upper[:,1]*scale, z_upper]
lower_3d = np.c_[lower[:,0]*scale, lower[:,1]*scale, z_lower]

# --- Plot ---
fig = go.Figure()

# S-curve
fig.add_trace(go.Scatter3d(
    x=X_s[:,0], y=X_s[:,1], z=X_s[:,2],
    mode='markers',
    marker=dict(size=2, color='blue'),
    name='S-Curve'
))

# Upper half moon
fig.add_trace(go.Scatter3d(
    x=upper_3d[:,0], y=upper_3d[:,1], z=upper_3d[:,2],
    mode='markers',
    marker=dict(size=2, color='green'),
    name='Upper Half Moon'
))

# Lower half moon
fig.add_trace(go.Scatter3d(
    x=lower_3d[:,0], y=lower_3d[:,1], z=lower_3d[:,2],
    mode='markers',
    marker=dict(size=2, color='red'),
    name='Lower Half Moon'
))

fig.update_layout(
    title='3D S-Curve with Upper and Lower Half Moons',
    scene=dict(aspectmode='data'),
    width=900, height=900
)
fig.show()
