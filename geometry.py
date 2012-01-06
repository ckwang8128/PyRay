"""
Class to represent the scene and shapes for raytracing
"""
from numpy import array,dot
import math
class Material:
    def __init__(self):
        self.color = (0,0,0)
        self.ambient = 0.0
        self.diffuse = 0.0
        self.specular = 0.0

    def set_color(self, rgb):
        """
        rgb is a 3-tuple that specifies red,green,blue values of a material
        """
        self.color = rgb

    def set_ambient(self, amb_val):
        self.ambient = amb_val
    
    def set_diffuse(self, diff_val):
        self.diffuse = diff_val
    
    def set_specular(self, spec_val):
        self.specular = spec_val
    
    def set_lighting(self, light_vals):
        """
        light_vals should be a 3-tuple of (ambient, diffuse, specular)
        """
        self.ambient, self.diffuse, self.specular = light_vals

    def get_lighting(self):
        """
        Returns a 3-tuple of (ambient, diffuse, specular)
        """
        return (self.ambient, self.diffuse, self.specular)



class Shape:
    """
    Basic class to represent a shape in a raytracing scene
    Class vars:
       pos = a 3-tuple representing the x,y,z position of the shape in space
    """
    def __init__(self, pos):
        self.pos = pos

    def set_position(self, pos):
        self.pos = pos

    def get_position(self):
        return self.pos

    def set_material(self, material):
        self.material = material

    def intersection(self, Ray):
        pass
    
    def get_color(self):
        return self.material.color

class Square(Shape):
    def intersection(self, Ray):
        pass

class Sphere(Shape):
    def __init__(self, center, radius):
        self.center = array(center)
        self.radius = float(radius)

    def intersects(self, ray):

        #a = d . d
        #b = 2 d . (p0 - pc)
        #c = (p0 - pc) . (p0 - pc) - r2

        p0 = ray.origin
        pc = self.center
        d = ray.direction
        r = self.radius

        a = dot(d,d)

        b = dot(2*d, p0-pc)
        c = dot((p0 - pc), (p0-pc)) - r**2
        try:

            val1 = (-b+math.sqrt(b**2 - (4*a*c)))/(2*a)
            val2 = (-b-math.sqrt(b**2 - (4*a*c)))/(2*a)
        except ValueError:
            return False
            
        return True

class Scene:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def get_width(self):
        return self.x

    def get_height(self):
        return self.y


