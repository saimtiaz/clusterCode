#! /usr/bin/env python
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pypcd import pypcd

def clusters2obj():
    pointCloudDir = 'clusterPC'
    fileList = os.listdir(pointCloudDir)
    objectList = []
    for file in fileList:
        if (file.endswith(".pcd")):
            fullFileName = os.path.join(pointCloudDir, file)
            pc = pypcd.PointCloud.from_path(fullFileName)

            allX = pc.pc_data['x']
            allY =  pc.pc_data['y']
            allZ = pc.pc_data['z']

            object = cluster2obj([allX, allY, allZ])
            objectList.append(object)

    return objectList




def cluster2obj(cluster):
    xS = cluster[0]
    yS = cluster[1]
    zS = cluster[2]

    minX = float(min(xS))
    maxX = float(max(xS))

    minY = float(min(yS))
    maxY = float(max(yS))

    minZ = float(min(zS))
    maxZ = float(max(zS))

    xScale = round(maxX - minX, 2)
    yScale = round(maxY - minY, 2)
    zScale = round(maxZ - minZ, 2)

    xTrans = round((maxX + minX)/2, 2)
    yTrans = round((maxY + minY)/2, 2)
    zTrans = round((maxZ + minZ)/2, 2)

    cube = {'type' : 'cuboid', 'scale' : [xScale, yScale, zScale], 
            'rotation' : [0.0, 0.0, 0.0], 'translation' : [xTrans, yTrans, zTrans]}

    # u = np.linspace(0, 2 * np.pi, 100)
    # v = np.linspace(0, np.pi, 100)
    # r = np.sqrt((minX - maxX)**2 + (minY - maxY)**2 + (minZ - maxZ)**2)
    # print(r)
    # x = r * np.outer(np.cos(u), np.sin(v)) + (minX + maxX)/2
    # y = r  * np.outer(np.sin(u), np.sin(v)) + (minY + maxY)/2
    # z = r  * np.outer(np.ones(np.size(u)), np.cos(v)) + (minZ + maxZ)/2
    # ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b', linewidth=0, alpha=0.5)
    # #calculate vectors for "vertical" circle

    return cube





