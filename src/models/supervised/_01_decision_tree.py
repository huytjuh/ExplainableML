import pandas as pd
import numpy as np

class PCA:
    """Principal Component Analysis (PCA) from scratch. Used for dimensionality reduction based on eigen decomposition of the covariance matrix"""

    def __init__(self, n_components: int=2):
        """initialize the PCA model with the number of principal components to keep."""
        self.n_components = n_components
        self.col_means = None
        self.components = None

    def fit(self, X: pd.DataFrame) -> 'PCA':
        """Fit the PCA model."""
        self.col_means = X.mean(axis=0)
        X_centered = X - self.col_means

        cov_matrix = np.cov(X_centered.T)
        eig_vals, eig_vecs = np.linalg.eigh(cov_matrix)
        idx = eig_vals.argsort()[::-1]
        eig_vals = eig_vals[idx]                    # magnitude of variance 
        eig_vecs = eig_vecs[:, idx]                 # direction of variance

        self.components = eig_vecs[:, :self.n_components]
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray:
        """Transform the input data using the fitted PCA model."""
        X_centered = X - self.col_means
        return X_centered @ self.components

    def explained_variance_ratio(self) -> np.ndarray:
        """Calculate the explained variance ratio for each principal component."""
        return self.components.T @ self.components
