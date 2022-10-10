import kmeans
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("./clustered-data.csv")
    dataset = df.values.tolist()

    k = kmeans.KMeans()
    k.fit(2, dataset, seed=45)

    print(k.get_centroids())
    print(k.get_repetitions())

    for centers, points in zip(k.get_centroids_history(), k.get_points_by_cluster_history()):
        points = []
        for c in centers:
            points.append(
                {
                    "center-index": c.get_index(),
                    "center": c.get_center_as_dict()
                }
            )

        print(points)

