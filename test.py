from objWriter import objWriter

def test_obj_write():
    #Create sample list of objects
    objects = [ {'type' : 'sphere', 'scale' : [2.5], 
                'rotation' : [0.0, 0.0, 0.0], 'translation' : [1.2, 1.2, 1.3]},
                {'type' : 'cuboid', 'scale' : [1.5, 2.5, 1.6], 
                'rotation' : [0.0, 0.0, 0.0], 'translation' : [0.2, -1.2, 1.3]},
                {'type' : 'sphere', 'scale' : [6.5], 
                'rotation' : [0.0, 0.0, 0.0], 'translation' : [-1.2, 1.2, 1.3]},
                {'type' : 'sphere', 'scale' : [0.5], 
                'rotation' : [0.0, 0.0, 0.0], 'translation' : [1.2, 1.2, -1.3]},
                {'type' : 'cuboid', 'scale' : [1.5, 2.5, 1.6], 
                'rotation' : [0.0, 0.0, 0.0], 'translation' : [-0.2, -1.2, 1.3]},
    ]

    #Call function
    objWriter(objects)



if __name__ == "__main__":
    #Create sample objects list
    test_obj_write()
    print("Everything passed")