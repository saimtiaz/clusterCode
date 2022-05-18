from objWriter import objWriter
from cluster2obj import cluster2obj, clusters2obj
import numpy as np
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pypcd import pypcd

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def display(self):
        print('x:', self.x, 'y:', self.y, 'z:', self.z)
    def distance(self, otherPoint):
        dist = (self.x - otherPoint.x)^2 + (self.y - otherPoint.y)^2 + (self.z - otherPoint.z)^2


def test_obj_write(objects):
    #Create sample list of objects
    # objects = [ {'type' : 'sphere', 'scale' : 2.5, 
    #             'rotation' : [0.0, 0.0, 0.0], 'translation' : [1.2, 1.2, 1.3]},
    #             {'type' : 'cuboid', 'scale' : [1.5, 2.5, 1.6], 
    #             'rotation' : [0.0, 0.0, 0.0], 'translation' : [0.2, -1.2, 1.3]},
    #             {'type' : 'sphere', 'scale' : 6.5, 
    #             'rotation' : [0.0, 0.0, 0.0], 'translation' : [-1.2, 1.2, 1.3]},
    #             {'type' : 'sphere', 'scale' : [0.5], 
    #             'rotation' : [0.0, 0.0, 0.0], 'translation' : [1.2, 1.2, -1.3]},
    #             {'type' : 'cuboid', 'scale' : [1.5, 2.5, 1.6], 
    #             'rotation' : [0.0, 0.0, 0.0], 'translation' : [-0.2, -1.2, 1.3]},
    # ]

    #Call function
    objWriter(objects)

def test_clusters2obj():
    objectList = clusters2obj()
    return objectList

def viz_clusters(objects):
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')

    pointCloudDir = 'clusterPC'
    fileList = os.listdir(pointCloudDir)
    for file in fileList:
        if (file.endswith(".pcd")):
            fullFileName = os.path.join(pointCloudDir, file)
            pc = pypcd.PointCloud.from_path(fullFileName)

            allX = pc.pc_data['x']
            allY =  pc.pc_data['y']
            allZ = pc.pc_data['z']

            ax.scatter(allX, allY, allZ)

    for object in objects:
        cornerPoints = getCorners(object)
        ax.scatter(cornerPoints[0], cornerPoints[1], cornerPoints[2])

    plt.show()
    
def getCorners(object):
    minX = object['translation'][0] - (object['scale'][0])/2
    maxX =  object['translation'][0] + (object['scale'][0])/2
    minY = object['translation'][1] - (object['scale'][1])/2
    maxY = object['translation'][1] + (object['scale'][1])/2
    minZ = object['translation'][2] - (object['scale'][2])/2
    maxZ = object['translation'][2] + (object['scale'][2])/2


    cornerPoints = [[minX, minX, minX, minX, maxX, maxX, maxX, maxX],
                    [minY, maxY, minY, maxY, minY, maxY, minY, maxY],
                    [minZ, minZ, maxZ, maxZ, minZ, minZ, maxZ, maxZ]
    ]
    return cornerPoints


if __name__ == "__main__":
    objects = clusters2obj()
    test_obj_write(objects)
    viz_clusters(objects)
    print("Everything passed")
