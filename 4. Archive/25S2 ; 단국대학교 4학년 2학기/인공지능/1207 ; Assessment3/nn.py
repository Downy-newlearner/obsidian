import numpy as np
import pandas as pd
from pathlib import Path


def euclidean_distances(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """a(테스트), b(학습) 사이의 모든 유클리드 거리 행렬 계산"""
    diff = a[:, None, :] - b[None, :, :]
    return np.sqrt(np.sum(diff * diff, axis=2))


def knn_predict(train_x, train_y, test_x, k: int) -> np.ndarray:
    """kNN 예측 함수"""
    dists = euclidean_distances(test_x, train_x)
    idx = np.argsort(dists, axis=1)[:, :k]   # 각 테스트 점에서 가장 가까운 k개
    knn_labels = train_y[idx]               # k개 이웃의 라벨
    # 다수결 투표
    preds = np.array([np.bincount(row).argmax() for row in knn_labels])
    return preds


def load_data():
    here = Path(__file__).parent
    train = pd.read_csv(here / "data" / "nntrain.csv", header=None).to_numpy()
    test = pd.read_csv(here / "data" / "nntest.csv", header=None).to_numpy()
    return train[:, :-1], train[:, -1].astype(int), test[:, :-1], test[:, -1].astype(int)


def evaluate_k(train_x, train_y, test_x, test_y, ks):
    results = []
    for k in ks:
        pred = knn_predict(train_x, train_y, test_x, k)
        acc = (pred == test_y).mean()
        results.append({"k": k, "accuracy": acc})
    return results


def main():
    train_x, train_y, test_x, test_y = load_data()
    ks = list(range(1, 16))
    results = evaluate_k(train_x, train_y, test_x, test_y, ks)

    for r in results:
        print(f"k={r['k']}: accuracy={r['accuracy']:.3f}")


if __name__ == "__main__":
    main()