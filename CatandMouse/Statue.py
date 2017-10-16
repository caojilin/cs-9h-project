from math import sin, cos, atan2, pi
from Turtle import Turtle
from Vector import *
from Color import *

class Statue(Turtle):
    """docstring for Statue."""
    def __init__(self, position, heading, speed=0, fill=blue, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.speed = speed

    def getshape(self):
        """Return a list of vectors giving the polygon for this turtle."""
        forward = unit(self.heading)
        right = unit(self.heading + 90)
        return [self.position + forward*100,
                self.position - right*100,
                self.position - forward*100,
                self.position + right*100]
