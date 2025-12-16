import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import common_utils

# ----------------------------------------------------------
#  Generate 3D Blob Dataset
# ----------------------------------------------------------
def generate_blob_data(n_samples=20000):
    centers = [[5, 5, 5], [-5, -5, -5], [5, -5, 5]]

    X, labels_true = make_blobs(
        n_samples=n_samples,
        centers=centers,
        cluster_std=0.6,
        random_state=42,
        n_features=3
    )

    # Standardize
    X = StandardScaler().fit_transform(X)

    return X, labels_true

# ----------------------------------------------------------
#  Add custom extra 3D points (in-between + global)
# ----------------------------------------------------------
def add_extra_points(X, labels_true, centers):
    P01 = common_utils.midpoint(centers[0], centers[1])
    P12 = common_utils.midpoint(centers[1], centers[2])
    P02 = common_utils.midpoint(centers[0], centers[2])
    P_global = (centers[0] + centers[1] + centers[2]) / 3.0

    extra_points = np.vstack([P01, P12, P02, P_global])

    labels_extra = np.full(extra_points.shape[0], 3)

    X_all = np.vstack([X, extra_points])
    y_all = np.concatenate([labels_true, labels_extra])

    return X_all, y_all, extra_points

# ----------------------------------------------------------
#  Compute cluster centers
# ----------------------------------------------------------
def compute_centers(X, labels_true):
    centers = {}
    for lbl in np.unique(labels_true):
        centers[lbl] = X[labels_true == lbl].mean(axis=0)
    return centers

# ----------------------------------------------------------
#  Full pipeline
# ----------------------------------------------------------
def run_pipeline(n_samples, prefix):
    X, labels_true = generate_blob_data(n_samples)
    centers = compute_centers(X, labels_true)
    X_all, y_all, extra_points = add_extra_points(X, labels_true, centers)
    fig = common_utils.create_3d_figure(X, labels_true,extra_points)
    common_utils.save_results(prefix, X_all, y_all, fig)

    return X_all, y_all, fig

# ----------------------------------------------------------
#  Run everything
# ----------------------------------------------------------
X_all, y_all, fig = run_pipeline( n_samples=20000,  prefix="blob_3_4IB" )