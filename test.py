from objWriter import objWriter
from cluster2obj import cluster2obj
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def display(self):
        print('x:', self.x, 'y:', self.y, 'z:', self.z)
    def distance(self, otherPoint):
        dist = (self.x - otherPoint.x)^2 + (self.y - otherPoint.y)^2 + (self.z - otherPoint.z)^2


def test_obj_write():
    #Create sample list of objects
    objects = [ {'type' : 'sphere', 'scale' : 2.5, 
                'rotation' : [0.0, 0.0, 0.0], 'translation' : [1.2, 1.2, 1.3]},
                {'type' : 'cuboid', 'scale' : [1.5, 2.5, 1.6], 
                'rotation' : [0.0, 0.0, 0.0], 'translation' : [0.2, -1.2, 1.3]},
                {'type' : 'sphere', 'scale' : 6.5, 
                'rotation' : [0.0, 0.0, 0.0], 'translation' : [-1.2, 1.2, 1.3]},
                {'type' : 'sphere', 'scale' : [0.5], 
                'rotation' : [0.0, 0.0, 0.0], 'translation' : [1.2, 1.2, -1.3]},
                {'type' : 'cuboid', 'scale' : [1.5, 2.5, 1.6], 
                'rotation' : [0.0, 0.0, 0.0], 'translation' : [-0.2, -1.2, 1.3]},
    ]

    #Call function
    objWriter(objects)

def test_cluster2obj():
    #p1 = Point3D(1,2,3)
    #p1.display()
    gaussDist = 0.2
    amountOfPoints = 200
    xsFront = (np.random.rand(amountOfPoints, 1) * 7) + (np.random.rand(amountOfPoints, 1) * gaussDist)
    ysFront = np.random.rand(amountOfPoints, 1) * 2 + (np.random.rand(amountOfPoints, 1) * gaussDist)
    zsFront = np.random.rand(amountOfPoints, 1) * 3 + (np.random.rand(amountOfPoints, 1) * gaussDist)

    xsTop = np.random.rand(amountOfPoints, 1) * 2 + (np.random.rand(amountOfPoints, 1) * gaussDist)
    ysTop = (np.random.rand(amountOfPoints, 1) * 0) + 1 + (np.random.rand(amountOfPoints, 1) * gaussDist)
    zsTop = np.random.rand(amountOfPoints, 1) * 2 + (np.random.rand(amountOfPoints, 1) * gaussDist)
    
    xsLeft = (np.random.rand(amountOfPoints, 1) * 3) + 7 + (np.random.rand(amountOfPoints, 1) * gaussDist)
    ysLeft = np.random.rand(amountOfPoints, 1)  + (np.random.rand(amountOfPoints, 1) * gaussDist)
    zsLeft = np.random.rand(amountOfPoints, 1) * 5 + (np.random.rand(amountOfPoints, 1) * gaussDist)

    #fig = plt.figure(figsize=(4,4))

    #ax = fig.add_subplot(111, projection='3d')

    allX = np.concatenate((xsFront, xsLeft, xsTop)) 
    allY = np.concatenate((ysFront, ysLeft, ysTop)) 
    allZ = np.concatenate((zsFront, zsLeft, zsTop)) 
    #ax.scatter(allX,allY,allZ) # plot the point (2,3,4) on the figure

    #plt.show()

    cluster = cluster2obj([allX, allY, allZ])
    print(cluster)
if __name__ == "__main__":
    #Create sample objects list
    #test_obj_write()
    test_cluster2obj()
    print("Everything passed")

