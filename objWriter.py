#! /usr/bin/env python

import os

def objWriter(objects):
    #Sort by cuboid and spheres
    cuboids = []
    spheres = []

    for object in objects:
        type = object['type']
        if type == 'sphere':
            spheres.append(object)
        elif type == 'cuboid':
            cuboids.append(object)

    #Remove existing settings.yaml
    settingsFileName = "settings.yaml"
    if (os.path.exists(settingsFileName)):
        os.remove(settingsFileName)
    else:
        print("The file", settingsFileName, "does not exist.")

    
    #objective_mode should be set to noECA if there are no objects
    numSpheres = len(spheres)
    numCubes = len(cuboids)
    objMode = ''
    if numSpheres + numCubes == 0:
        objMode = 'noECA'
    else:
        objMode = 'ECAA'

    #Create header of the settings.yaml
    linkRadius = 0.05
    name = 'ur5_info.yaml'
    inputDevice = 'keyboard'

    f = open(settingsFileName, 'w')
    f.write('loaded_robot:\n')
    f.write('  name: ' + name + '\n')
    f.write('  link_radius: ' + str(linkRadius) + '\n')
    f.write('  objective_mode: ' + objMode + '\n')
    f.write('  input_device: ' + inputDevice + '\n')
    f.write('obstacles:\n')
    
    #Write the cuboids header if there are cuboids
    #For loop and write each cuboid
    #For loop and write each sphere

    f.close()
