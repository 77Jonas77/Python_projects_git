import math
import random
from collections import Counter

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
        self.initialize_vectors()
        self.initialize_centroids()
        self.assign_clusters_randomly()
        self.sums_of_clusters: list[float] = None

    def __str__(self) -> None:
        for i in range(len(self.centroids)):
            print(f"Centroid: {i}: S= {self.sums_of_clusters[i]}")

    def update_sums_of_clusters(self) -> None:
        """Updating the sum of squares of distances from centroids"""
        self.sums_of_clusters = [0] * len(self.centroids)
        for i, centroid in enumerate(self.centroids):
            sum_of_squares = 0
            for vector in self.vectors:
                if vector[-1] == i:
                    dist = np.linalg.norm(np.array(vector[:-2])
                                          - np.array(centroid))
                    sum_of_squares += dist
            self.sums_of_clusters[i] = sum_of_squares

    def print_clusters_contents(self) -> None:
        """Calculates entropy for clusters based on species"""
        print("=================")
        for centroid_index in range(self.k):
            cluster_species = [vector[-2] for vector in self.vectors if
                               vector[-1] == centroid_index]
            species_counts = Counter(cluster_species)
            total_count = sum(species_counts.values())
            print(f"Centroid: {centroid_index} ==== Species: {total_count}")
            print(f"Specie: 1gr\t\t\t 2gr\t\t\t\t\t 3gr \t\t\t\t\t")
            for specie, count in species_counts.items():
                print(f"{specie}: {count}", end='\t')

            entropy = 0
            for count in species_counts.values():
                p = count / total_count
                entropy -= p * math.log2(p)
            print(f"Entropy: {entropy}")
            print('\n' * 2)
        print("=================")

    def calculate_centroid_for_all_clusters(self) -> None:
        """Calculating centroids for each group"""
        self.centroids = []
        for i in range(self.k):
            # retrieving all data for specified group
            cluster_points = np.array(
                [vector[:-2] for vector in self.vectors if vector[-1] == i])
            if len(cluster_points) > 0:
                # avg for every column (x1,x2,x3)
                centroid = np.mean(cluster_points, axis=0)
                self.centroids.append(centroid)
            else:
                self.centroids.append(np.array(choice(self.vectors)[:-2]))

    def assign_clusters_randomly(self) -> None:
        """Assigning random clusters to vectors"""
        for vector in self.vectors:
            vector.append(random.randint(0, self.k - 1))

    def assign_clusters(self) -> None:
        """Assigning clusters to data points"""
        for vector in self.vectors:
            min_dist = float('inf')
            closest_centroid = None
            for indx, centroid in enumerate(self.centroids):
                # Euclidean distance
                dist = np.linalg.norm(
                    np.array(vector[:-2]) - np.array(centroid))
                if dist < min_dist:
                    min_dist = dist
                    closest_centroid = indx
            vector[-1] = closest_centroid

    def initialize_vectors(self) -> None:
        """Initialization of vectors"""
        for index, row in self.data.iterrows():
            self.vectors.append(row.tolist())

    def initialize_centroids(self) -> None:
        """Initialization of centroids"""
        for _ in range(self.k):
            self.centroids.append(choice(self.vectors))
