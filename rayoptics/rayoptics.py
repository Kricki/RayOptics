import numpy as np


class Ray:
    def __init__(self, height=0, angle=0):
        self.height = height
        self.angle = angle

    def rotate(self, angle):
        self.angle += angle

    def refract(self, n1, n2, tilt=0):
        self.rotate(tilt)
        self.angle = np.arcsin(n1/n2*np.sin(self.angle))
        self.rotate(-tilt)

    def translate(self, distance):
        self.height += np.tan(self.angle)*distance
 
    def transmit(self, thickness, tilt):
        self.height += np.sin(self.angle)*thickness/(np.cos(self.angle+tilt))
