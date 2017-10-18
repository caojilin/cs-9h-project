from Turtle import Turtle
from Vector import *
from Color import *
import math

scale_factor = 50       # 1 meter = scale_factor pixels

class Statue(Turtle):       #### Inherit behavior from Turtle
    """The statue that is stationary."""

    def __init__(self, position, fill=green, **style):
        """Initiates the turle with heading 0 and calls turtle init method."""
        heading = 0
        Turtle.__init__(self, position, heading, fill=fill, **style)

    def getnextstate(self):
        """No movement."""
        return self.position, self.heading

    def reset(self):
        """Resets the position of the statue to its original position (should be no change)."""
        heading = 0

    def getshape(self):
        """
        Return a list of vectors giving the polygon for this statue.
        Returns a list of coordinates on a circle at 10 degree increments of all 360 degrees.
        """
        coords = []
        for i in range(0,360,10):
            angle = i * pi/180
            coords = coords + [Vector(200 + scale_factor*math.cos(angle), 200 + scale_factor*math.sin(angle))]
        return coords
