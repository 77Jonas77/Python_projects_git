from collections import Counter
from copy import deepcopy
import numpy as np
import pandas as pd
from random import choice


class KMeans:
    """
    on -1 index -> cluster
    on -2 index -> decision
    """

    def __init__(self, k: int, data: pd.DataFrame) -> None:
        self.k = k
        self.data = data
        self.vectors: list = []
        self.centroids: list = []
        self.clusters = []
        self.initialize_vectors()
        self.initialize_centroids()

    @staticmethod
    def squared_distance(data_point, centroids) -> float:
        return np.linalg.norm(np.array(centroids) - np.array(data_point))

    def assign_clusters(self) -> int:
        """Assigning clusters to data points"""
        c = 0
        for vector in self.vectors:
            min_dist = float('inf')
            closest_centroid = None
            for indx, centroid in enumerate(self.centroids):
                # Euclidean distance
                if len(centroid) > 4:
                    centroid = centroid[:-2]
                dist = self.squared_distance(vector[:-2], centroid)
                if dist < min_dist:
                    min_dist = dist
                    closest_centroid = indx
            if closest_centroid != vector[-1] and vector[-1] != -1:
                self.clusters[vector[-1]].remove(vector)
                vector[-1] = closest_centroid
                self.clusters[closest_centroid].append(vector)
                c += 1
            elif vector[-1] == -1:
                vector[-1] = closest_centroid
                self.clusters[closest_centroid].append(vector)
                c += 1
        return c

    def initialize_vectors(self) -> None:
        """Initialization of vectors"""
        for index, row in self.data.iterrows():
            self.vectors.append(row.tolist())

        for vec in self.vectors:
            vec.append(-1)

    def initialize_centroids(self) -> None:
        """Initialization of centroids"""
        available_vectors = self.vectors[:]
        for i in range(self.k):
            vector = choice(available_vectors)
            self.centroids.append(deepcopy(vector))

            available_vectors.remove(vector)
            self.clusters.append([])

    def update_centroids(self):
        for i in range(self.k):
            group = self.clusters[i]

            if not group:
                continue

            new_centroid_coordinates = [0.0] * len(self.vectors[0][:-2])

            for observation in group:
                for j, coordinate in enumerate(observation[:-2]):
                    new_centroid_coordinates[j] += coordinate

            for j in range(len(self.vectors[0][:-2])):
                new_centroid_coordinates[j] /= len(group)

            self.centroids[i] = new_centroid_coordinates

    def print_clusters(self) -> None:
        """Print contents of clusters"""
        for i, cluster in enumerate(self.clusters):
            print(f"Cluster {i}:")
            decision_counts = Counter(vector[-2] for vector in cluster)
            for decision, count in decision_counts.items():
                print(f"Decision: {decision}, Count: {count}")
            print()

    def run(self) -> None:
        counter = None
        while counter is None or counter != 0:
            counter = self.assign_clusters()
            self.update_centroids()
        self.print_clusters()
