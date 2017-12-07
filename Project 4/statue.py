from Turtle import Turtle
from math import cos, sin, pi
from Vector import *
from Color import *

scalar = 50

class Statue(Turtle):
    """a circular Statue doesn't move"""
    def __init__(self, position,fill=red):
        heading = 0
        self.position = position
        self.radius = 1
        Turtle.__init__(self, position, heading, fill=fill)

    def getshape(self):
        """Return a list of vectors giving the polygon for this turtle"""
        coords = []
        for i in range(0, 360, 10):
            angle = pi * i/180
            coords = coords + [self.position + Vector(scalar * cos(angle), scalar * sin(angle))]
        return coords
