"""

Class for keeping track of all of the elements of a scene
Shapes
Lights
Camera position


"""


class Scene:
    def __init__(self, f_name):
        """
        Loads and creates a scene from a file
        """
        self.lights = []
        self.shapes = []
        self.camera = None
