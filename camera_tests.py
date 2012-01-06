import unittest
from ray import Camera

class CameraTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_basic(self):
        cam = Camera(200,200)
        print cam.fovx


if __name__ == '__main__':
    unittest.main()
