import random
import numpy as np
import pandas as pd
from random import choice


class KMeans:
    def __init__(self, k: int, data: pd.DataFrame):
        self.k = k
        self.data = data
        self.vectors = []
        self.centroids = []
        self.initialize_vectors()
        self.initialize_centroids()
        self.assign_clusters_randomly()
        # print(self.vectors)

    def calculate_centroid_for_group(self):
        """Calculating centroids for each group"""
        self.centroids = []
        for i in range(self.k):
            # retriving all data for specified group
            cluster_points = [list(vector[:-2]) for vector in self.vectors if
                              vector[-1] == i]
            if len(cluster_points) > 0:
                # avg for every column (x1,x2,x3)
                centroid = np.mean(cluster_points, axis=0)
                self.centroids.append(centroid)
            else:
                self.centroids.append(choice(self.vectors)[:-2])

    def assign_clusters_randomly(self):
        """Assigning random clusters to vectors"""
        for vector in self.vectors:
            vector.append(random.randint(0, self.k - 1))

    def assign_clusters(self):
        """Assigning clusters to data points"""
        for vector in self.vectors:
            min_dist = float('inf')
            closest_centroid = None
            for indx, centroid in enumerate(self.centroids):
                # Euclidean distance
                dist = np.linalg.norm(
                    np.array(vector[:-1]) - np.array(centroid))
                if dist < min_dist:
                    min_dist = dist
                    closest_centroid = indx
            vector[-1] = closest_centroid

    def initialize_vectors(self):
        """Initialization of vectors"""
        for index, row in self.data.iterrows():
            self.vectors.append(row.tolist())

    def initialize_centroids(self):
        """Initialization of centroids"""
        for _ in range(self.k):
            self.centroids.append(choice(self.vectors))
