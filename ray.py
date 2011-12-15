from numpy import array

class Ray:
    
    def __init__(self):
        self.origin = array([0,0,0])
        self.direction = array([0,0,0])

    def __init__(self, origin, direction):
        self.origin = array(origin)
        self.direction = array(direction)


class Camera:
    def __init__(self):
        pass

    def get_ray(self):
        pass
    
