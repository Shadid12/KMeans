from points import *
from readData import ReadData
import csv
from kmeans import *


# read the data first 
r = ReadData('exercise-1.csv')
data = r.read()
# print (data)

# make points array

points = []
for arr in data:
    p = Point(arr[0], arr[1])
    points.append(p)

# generate random centroids 
k = Kmeans(2, points)
k.gen_random_centroids()

while not k.converge():
    k.group_points()
    k.reassign()

for c in k.centroids:
    x = []
    y = []
    for p in k.data:
        if p.get_centroid().get_x() == c.get_x() and p.get_centroid().get_y() == c.get_y():
          x.append(p.get_x())
          y.append(p.get_y())
    print (x, y)
