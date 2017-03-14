from readData import ReadData

'''
This class represents a Point
a Point has x, y cordinates and a Centroid
'''
class Point:
    
    def __init__(self, x, y, centroid=None):
        self.x = x
        self.y = y
        self.centroid = centroid
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_centroid(self):
        return self.centroid
        
    def set_centroid(self, c):
        self.centroid = c
    

'''
This class represents a Centroid
a Centroid has x, y cordinate
'''
class Centroid:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    