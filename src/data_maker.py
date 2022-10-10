"""Utility to create testing data to use for k-means training."""

from sklearn.datasets import make_blobs


def make_data(filename, n_clusters, n_samples=100, n_features=2, stdev=5.):

    with open(filename, 'w') as f:
        tokens = [f"X{i + 1}" for i in range(n_features)]
        f.write(",".join(tokens))
        f.write("\n")
        print(",".join(tokens))

        features, _ = make_blobs(
            n_samples=n_samples,
            n_features=n_features,
            centers=n_clusters,
            cluster_std=stdev,
            shuffle=True
        )

        for v in features.tolist():
            tokens = [f"{x:.4f}" for x in v]
            print(','.join(tokens))
            f.write(",".join(tokens))
            f.write("\n")


if __name__ == '__main__':
    make_data("clustered-data.csv", n_clusters=4, n_samples=5000)
