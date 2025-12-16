import numpy as np
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split

import common_utils

# ----------------------------------------------------------
#  Generate dataset
# ----------------------------------------------------------
def generate_blob_dataset(n_samples=50000, random_state=42):
    centers = [(-5, -5, -5), (5, 5, 5)]

    X, y = make_blobs(
        n_samples=n_samples,
        centers=centers,
        n_features=3,
        shuffle=False,
        random_state=random_state
    )

    # Fix labels
    y[: n_samples // 2] = 0
    y[n_samples // 2:] = 1

    # Random weights
    sw = np.random.RandomState(random_state).rand(len(y))

    return X, y, sw

# ----------------------------------------------------------
#  End-to-end pipeline
# ----------------------------------------------------------
def generate_and_save(n_samples=5000,prefix='data'):
    X, y, sw = generate_blob_dataset(n_samples=n_samples)

    # Train/test split (we only plot train)
    X_train, _, y_train, _, sw_train, _ = train_test_split(X, y, sw, test_size=0.9, random_state=42)
    extra_points = np.array([ [0, 0, 0] ])
    fig = common_utils.create_3d_figure(X, y,sw, extra_points)
    common_utils.save_results(prefix, X, y, fig)

    return X, y, sw, fig

# ----------------------------------------------------------
#  Run it
# ----------------------------------------------------------
X, y, sw, fig = generate_and_save(n_samples=20000,prefix="blob_2_1IB")