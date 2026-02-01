import numpy as np
import pandas as pd
from pathlib import Path


def load_data():
    train = pd.read_csv("data/rtrain.csv", header=None).to_numpy()
    test = pd.read_csv("data/rtest.csv", header=None).to_numpy()

    train_x = train[:, :-1]
    train_y = train[:, -1]

    test_x = test[:, :-1]
    test_y = test[:, -1]

    return train_x, train_y, test_x, test_y


def add_bias(x):
    """bias 항 추가: [x] → [1, x]"""
    return np.hstack([np.ones((x.shape[0], 1)), x])


def train_linear_regression(x, y):
    """Least Square Normal Equation"""
    X = add_bias(x)
    theta = np.linalg.inv(X.T @ X) @ X.T @ y
    return theta


def predict(x, theta):
    X = add_bias(x)
    return X @ theta


def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def main():
    train_x, train_y, test_x, test_y = load_data()

    theta = train_linear_regression(train_x, train_y)
    pred = predict(test_x, theta)
    loss = mse(test_y, pred)

    print("Learned θ:", theta)
    print("Test MSE:", loss)


if __name__ == "__main__":
    main()