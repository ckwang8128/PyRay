"""
Class to represent the scene and shapes for raytracing
"""


class Material:
    def __init__(self):
        self.color = (0,0,0)
        self.ambient = 0.0

    def set_color(self, rgb):
        """
        rgb is a 3-tuple that specifies red,green,blue values of a material
        """
        self.color = rgb

    def set_ambient(self, amb_val):
        self.ambient = amb_val
    
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

class Square(Shape):
    pass

class Sphere(Shape):
    pass


class Scene:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def get_width(self):
        return self.x

    def get_height(self):
        return self.y


