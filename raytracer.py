import sys
from ray import *
from geometry import *
from render import *
import Image





if __name__ == '__main__':
    #Read in the file, do it later
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    my_scene = Scene(width,height)
    picture = Image.new('RGB', (width, height))
    pixels = picture.load()
    my_cam = Camera(height, width)


    #hardcode a shape in right now. 
    shapes = []
    sphere = Sphere([0,0,-2], 1)
    sphere2 = Sphere([1,0,-3], 1)
    mat1 = Material()
    mat1.set_color((125,0,0))
    mat1.set_lighting((1,0.5,0.5))

    sphere.set_material(mat1)



    mat2 = Material()
    mat2.set_color((0,125,0))
    mat2.set_lighting((1,0.5,0.5))


    sphere.set_material(mat1)
    sphere2.set_material(mat2)
    shapes.append(sphere)
    shapes.append(sphere2)

    
    for i in range(0, my_scene.get_width()):
        for j in range(0, my_scene.get_height()):
            #Want to do ray tracing here
            ray = my_cam.get_ray((i,j))
            import random
            counter = 0
            for shape in shapes:
                counter += 1
                if shape.intersects(ray):
                    r,g,b = shape.get_color()
                    pixels[i,j] = (r,g,b)
    #         pixels[i,j] = (random.randint(0,255),
    #                        random.randint(0,255),
    #                        random.randint(0,255))
    picture.show()
