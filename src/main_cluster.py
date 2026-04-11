import pandas as pd
import numpy as np 

from models.unsupervised._01_pca import PCA

if __name__ == "__main__":

    data = pd.read_csv('data/heart.csv')

    X = data.iloc[:, :-1]
    X_encoded = pd.get_dummies(X, drop_first=True).astype(float)

    PCA = PCA(n_components=2)
    PCA_fit = PCA.fit(X_encoded)
    X_reduced = PCA_fit.transform(X_encoded)

    print(X_reduced)
    