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
    
    for i in range(0, my_scene.get_width()):
        for j in range(0, my_scene.get_height()):
            #Want to do ray tracing here
            import random
            pixels[i,j] = (random.randint(0,255),
                           random.randint(0,255),
                           random.randint(0,255))
    picture.show()
