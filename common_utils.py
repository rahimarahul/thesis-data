import plotly.graph_objects as go
import os
import numpy as np
# ----------------------------------------------------------
#  Create 3D figure
# ----------------------------------------------------------
def create_3d_figure(X_train, y_train,extra_points):
    fig = go.Figure()

    fig.add_trace(go.Scatter3d(
        x=X_train[:, 0],
        y=X_train[:, 1],
        z=X_train[:, 2],
        mode="markers",
        marker=dict(
            size=3,
            color=y_train,
            colorscale="Viridis",
            opacity=0.7,
        ),
        name="Blob Points",
    ))
    # Extra in-between points
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

    fig.update_layout(
        title="3D Blob Dataset with In-Between Point",
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z",
            aspectmode="data"
        ),
        legend=dict(x=0.02, y=0.98)
    )
    fig.show()
    return fig
def midpoint(a, b):
    return (a + b) / 2.0

# ----------------------------------------------------------
#  Save dataset + figure
# ----------------------------------------------------------
def save_results(prefix, X_all, y_all, fig, folder="data"):
    os.makedirs(folder, exist_ok=True)

    npz_path = os.path.join(folder, f"{prefix}.npz")
    html_path = os.path.join(folder, f"{prefix}.html")
    png_path = os.path.join(folder, f"{prefix}.png")

    # Save dataset
    np.savez(npz_path, X=X_all, y=y_all)
    fig.write_html(html_path)
    fig.write_image(png_path, scale=3)

