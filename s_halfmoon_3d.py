import numpy as np
import plotly.graph_objects as go

# Parameters
r = 1.0         # radius of arcs
n = 2000        # points per section (spine)
tube_points = 20  # points around the spine cross-section
tube_radius = 0.5  # thickness of the tube
gap = 0.1

# --- Helper function to generate scatter points around a 3D spine ---
def tubular_scatter(x_spine, y_spine, z_spine, tube_radius, tube_points):
    points = []
    for xi, yi, zi in zip(x_spine, y_spine, z_spine):
        # Random angle around spine for circular cross-section
        theta = np.random.uniform(0, 2*np.pi, tube_points)
        r_rand = tube_radius * np.random.rand(tube_points)
        cx = xi + r_rand * np.cos(theta)
        cy = yi + r_rand * np.sin(theta)
        cz = zi + r_rand * np.sin(theta/2)  # small z offset
        points.append(np.c_[cx, cy, cz])
    return np.vstack(points)

# -------------------------
# Top half-circle
theta_top = np.linspace(0, np.pi, n)
x_top = r * np.cos(theta_top)
y_top = r * np.sin(theta_top) + 2*r + gap
z_top = np.linspace(0.2, 1.0, n)
top_scatter = tubular_scatter(x_top, y_top, z_top, tube_radius, tube_points)

# -------------------------
# Middle S-curve (two connected half-circles)
theta1 = np.linspace(np.pi/2, 3*np.pi/2, n)
x1 = r * np.cos(theta1)
y1 = r * np.sin(theta1)
z1 = np.linspace(0.4, 0.7, n)

theta2 = np.linspace(3*np.pi/2, 5*np.pi/2, n)
x2 = r * np.cos(theta2)
y2 = r * np.sin(theta2) - 2*r
z2 = np.linspace(0.4, 0.7, n)

x_s = np.concatenate([x1, x2])
y_s = np.concatenate([y1, y2])
z_s = np.concatenate([z1, z2])
s_scatter = tubular_scatter(x_s, y_s, z_s, tube_radius, tube_points)

# -------------------------
# Bottom half-circle
theta_bottom = np.linspace(np.pi, 2*np.pi, n)
x_bottom = r * np.cos(theta_bottom)
y_bottom = r * np.sin(theta_bottom) - 4*r - gap
z_bottom = np.linspace(0.0, 1.0, n)
bottom_scatter = tubular_scatter(x_bottom, y_bottom, z_bottom, tube_radius, tube_points)

# -------------------------
# Plotly 3D scatter
fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=top_scatter[:,0], y=top_scatter[:,1], z=top_scatter[:,2],
    mode='markers',
    marker=dict(size=1.5, color='red'),
    name='Top Half-Circle'
))

fig.add_trace(go.Scatter3d(
    x=s_scatter[:,0], y=s_scatter[:,1], z=s_scatter[:,2],
    mode='markers',
    marker=dict(size=1.5, color='blue'),
    name='Middle S-Curve'
))

fig.add_trace(go.Scatter3d(
    x=bottom_scatter[:,0], y=bottom_scatter[:,1], z=bottom_scatter[:,2],
    mode='markers',
    marker=dict(size=1.5, color='green'),
    name='Bottom Half-Circle'
))

fig.update_layout(
    title='3D Scatter Tubular S-Curve with Top/Bottom Half-Circles',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectmode='data'
    ),
    width=900,
    height=900
)

fig.show()