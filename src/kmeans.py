import copy
import math
import random
import sys


def euclidean_distance(p1, p2):
    assert len(p1) == len(p2) == 2
    x1, y1 = p1
    x2, y2 = p2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class Centroid:
    def __init__(self, index, center):
        assert isinstance(center, tuple) and len(center) == 2
        self.__center = copy.deepcopy(center)
        self.__index = index

    def __repr__(self):
        return f"{self.__index} ({self.__center[0]}, {self.__center[1]})"

    def get_index(self):
        return self.__index

    def get_distance(self, point):
        return euclidean_distance(self.__center, (point.x, point.y))

    def set_center(self, center):
        self.__center = center

    def get_center(self):
        return copy.deepcopy(self.__center)

    def get_center_as_dict(self):
        return {
            "x": self.__center[0],
            "y": self.__center[1],
        }


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__centroid_id = None

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def centroid_id(self):
        return self.__centroid_id

    @centroid_id.setter
    def centroid_id(self, value):
        self.__centroid_id = value


class KMeans:

    def __init__(self):
        self.__points = None
        self.__centroids = None
        self.__repetitions = None

    def fit(self, n_cluster_count, dataset, seed=None):
        dataset1 = []
        for v in dataset:
            dataset1.append(tuple(v))
        dataset = dataset1
        assert len(dataset) > n_cluster_count >= 1
        self.__points = [Point(x, y) for x, y in dataset]
        d = copy.deepcopy(dataset)
        if seed:
            random.seed(seed)
        random.shuffle(d)
        self.__centroids = [Centroid(i, d[i]) for i in range(n_cluster_count)]

        self.__centroid_history = []
        self.__centroid_history.append(copy.deepcopy(self.__centroids))
        self.__clustered_points_history = []
        self.__points_by_cluster_history = []

        self.__repetitions = 0
        while self.iterate():
            self.__centroid_history.append(copy.deepcopy(self.__centroids))
            self.__points_by_cluster_history.append(
                copy.deepcopy(self.group_points_by_cluster()))
            self.__repetitions += 1

    def get_centroids_history(self):
        return copy.deepcopy(self.__centroid_history)

    def get_points_by_cluster_history(self):
        return copy.deepcopy(self.__points_by_cluster_history)

    def get_centroids(self):
        return copy.deepcopy(self.__centroids)

    def get_repetitions(self):
        return self.__repetitions

    def group_points_by_cluster(self):
        points_by_cluster = {}
        for p in self.__points:
            if p.centroid_id not in points_by_cluster:
                points_by_cluster[p.centroid_id] = []

            points_by_cluster[p.centroid_id].append((p.x, p.y))

        return points_by_cluster

    def iterate(self):
        centroids_before = []

        for c in self.__centroids:
            center = c.get_center()
            centroids_before.append(center[0])
            centroids_before.append(center[1])

        for point in self.__points:
            min_distance = sys.float_info.max
            for centroid in self.__centroids:
                d = centroid.get_distance(point)
                if d < min_distance:
                    min_distance = d
                    point.centroid_id = centroid.get_index()

        points_per_centroid = {c.get_index(): [] for c in self.__centroids}

        for p in self.__points:
            points_per_centroid[p.centroid_id].append(p)

        for centroid_id, points in points_per_centroid.items():
            total_x = sum(p.x for p in points)
            total_y = sum(p.y for p in points)
            c = (total_x / len(points), total_y / len(points))
            self.__centroids[centroid_id].set_center(c)

        centroids_after = []

        for c in self.__centroids:
            center = c.get_center()
            centroids_after.append(center[0])
            centroids_after.append(center[1])

        moved = False
        for v1, v2 in zip(centroids_before, centroids_after):
            diff = math.fabs(v1 - v2)
            if diff >= 0.001:
                moved = True
        return moved
