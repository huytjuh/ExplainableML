import pandas as pd
import numpy as np

class PCA:
    """Principal Component Analysis (PCA) from scratch. Used for dimensionality reduction based on eigen decomposition of the covariance matrix"""

    def __init__(self, n_components: int=2):
        self.n_components = n_components

    def fit(self, X: pd.DataFrame) -> 'PCA':
        """Fit the PCA model."""

        pass 

    def transform(self, X: pd.DataFrame) -> np.ndarray:
        pass
