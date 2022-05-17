#! /usr/bin/env python

import os


def objWriter(objects):
    #Sort by cuboid and spheres
    cuboids = []
    spheres = []

    for object in objects:
        objClass = object['type']
        if objClass == 'sphere':
            spheres.append(object)
        elif objClass == 'cuboid':
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
    
    #For loop and write each cuboid
    if numCubes > 0:
        f.write('  cuboids:\n')
        counter = 1
        for cube in cuboids:
            cubeName = 'box' + str(counter)
            cubeScale = str(cube['scale'])
            cubeTrans = str(cube['translation'])
            cubeRot = str(cube['rotation'])
            animation = 'static'

            f.write('    - name: ' + cubeName + '\n')
            f.write('      scale: ' + cubeScale + '\n')
            f.write('      translation: ' + cubeTrans + '\n')
            f.write('      rotation: ' + cubeRot + '\n')
            f.write('      animation: ' + animation + '\n')

            counter = counter + 1
    #For loop and write each sphere
    if numSpheres > 0:
        f.write('  spheres:\n')
        counter = 1
        for sphere in spheres:
            sphereName = 'sphere' + str(counter)
            scale = sphere['scale']
            if type(scale) is list:
                scale = sphere['scale'][0]
            sphereScale = str(scale)
            sphereTrans = str(sphere['translation'])
            sphereRot = str(sphere['rotation'])
            animation = 'static'

            f.write('    - name: ' + sphereName + '\n')
            f.write('      scale: ' + sphereScale + '\n')
            f.write('      translation: ' + sphereTrans + '\n')
            f.write('      rotation: ' + sphereRot + '\n')
            f.write('      animation: ' + animation + '\n')

            counter = counter + 1

    f.close()
