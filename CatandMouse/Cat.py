from math import sin, cos, atan2, pi
from Turtle import Turtle
from Vector import *
from Color import *

class Cat(Turtle):
    """Cat class"""
    def __init__(self, position, heading, speed=0, fill=blue, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.speed = speed
def getshape(self):
    """Return a list of vectors giving the polygon for this turtle."""
    forward = unit(self.heading)
    right = unit(self.heading + 90)
    return [self.position + forward*15,
            self.position - forward*8 - right*8,
            self.position - forward*5,
            self.position - forward*8 + right*8]
