from points import *
import math
import random

class Kmeans:
    
    
    
    def __init__(self, cluster_num, data):
        self.cluster_num = cluster_num
        self.data = data
        self.centroids = []
        self.old_centroids = []
        
    
    # This func will generate c numbers of random centroids
    def gen_random_centroids(self):
        c = 0
        x_cordinates = []
        y_cordinates = []
        # go over all the points and find minimum x, y and maximum x,y
        for val in self.data:
            x_cordinates.append(val.get_x())
            y_cordinates.append(val.get_y())
        
        x_min = min(x_cordinates)
        x_max =max(x_cordinates)
        y_min = min(y_cordinates)
        y_max =max(y_cordinates)
        
        while c < self.cluster_num:
            random_x = random.uniform(x_min, x_max)
            random_y = random.uniform(y_min, y_max)
            random_centroid = Centroid(random_x, random_y)
            self.centroids.append(random_centroid)
            c += 1
        
    
    def eucledian_distance(self, x1, y1, x2, y2):
        xx = ( x1 - x2 ) ** 2
        yy = ( y1 - y2 ) ** 2
        return ( round (math.sqrt(xx + yy), 2) )
    
    def group_points(self):
        
        for point in self.data:
            x_cor = point.get_x()
            y_cor = point.get_y()
            min_eucledian_distance = None
            
            for centroid in self.centroids:
                c_x = centroid.get_x()
                c_y = centroid.get_y()
                dis = self.eucledian_distance(x_cor, y_cor, c_x, c_y)
                if min_eucledian_distance is None:
                    min_eucledian_distance = dis
                    point.set_centroid(centroid)
                if min_eucledian_distance > dis:
                    min_eucledian_distance = dis
                    point.set_centroid(centroid)
    
    def getAverage(self, x):
        s = 0
        for val in x:
            s = s + val
        return (round (s / len(x), 2 ))
    
    def reassign(self):
        x = []
        y = []
        new_centroids = []
        for centroid in self.centroids:
            for point in self.data:
                if point.get_centroid() == centroid:
                    x.append(point.get_x())
                    y.append(point.get_y())
            avg_x = self.getAverage(x)
            avg_y = self.getAverage(y)
            new_centroid = Centroid(avg_x, avg_y)
            new_centroids.append(new_centroid)
            x = []
            y = []
        self.old_centroids = self.centroids
        self.centroids = new_centroids
        
        for val in self.old_centroids:
            print (val.get_x(), val.get_y())
        for val in self.centroids:
            print (val.get_x(), val.get_y())
        print ("### Iteration done ####")
    
    
    def converge(self):
        sumA = 0
        sumB = 0
        for i in self.centroids:
            sumA = sumA + i.get_x() + i.get_y()
        for i in self.old_centroids:
            sumB = sumB + i.get_x() + i.get_y()
        return sumA == sumB
            