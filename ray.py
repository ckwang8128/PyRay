from numpy import array, tan
from math import pi

class Ray:
    
    def __init__(self):
        self.origin = array([0,0,0])
        self.direction = array([0,0,0])

    def __init__(self, origin, direction):
        self.origin = array(origin)
        self.direction = array(direction)


class Camera:
    def __init__(self, height, width):
        """
        Camera takes in the height and width of the image to be produced 
        in pixel size.
        """
        self.height = height
        self.width = width
        self.fovx = float(pi/4)
        self.fovy = (float(height)/width) * self.fovx
        
        #Precompute these for ray operations
        self.tan_fovx = float(tan(self.fovx))
        self.tan_fovy = float(tan(self.fovy))

        #Will initially keep camera at 0,0,0
        self.position = [0,0,0]
        
    def get_ray(self, pixel_coordinates):
        """
        pixel_coordinates: 2-D tuple consisting of x,y coordinates of pixel
        in final output image. 
        """
        u_pixel = float(pixel_coordinates[0])
        v_pixel = float(pixel_coordinates[1])
        
        x = ((2*u_pixel - self.width)/self.width) * self.tan_fovx
        y = ((2*v_pixel - self.height)/self.height) * self.tan_fovy

        return Ray(self.position, [x,y,-1])
    
