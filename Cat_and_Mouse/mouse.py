from Turtle import Turtle
from Vector import *
from Color import *
from statue import scale_factor
import math

class Mouse(Turtle):       #### Inherit behavior from Turtle
    """The mouse that circles the statue."""

    def __init__(self, heading, statueObj, fill=blue, **style):
        """
        Create mouse with given heading. Calls turtle init function.
        """
        self.heading = heading
        self.originalHeading = heading
        self.originalColor = fill
        # coordinate formula is ( r * cos(angle), r * sin(angle) )
        position = Vector(200 + scale_factor * math.cos(heading*pi/180), 200 + scale_factor * math.sin(heading*pi/180))
        self.originalPosition = position
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.statueObj = statueObj

    def getnextstate(self):
        """Circles around statue, 1 meter every minute."""
        # angle change @ = distance around cirlce / radius of circle
        # x' = x cos @ - y sin @
        # y' = x sin @ + y cos @
        angle = 1 * 180/pi * 1/60 # in degrees, (always 1 because distance/radius = 1), 1 second = 1 frame
        self.heading -= angle # change the heading by calculated angle
        angle_change = -angle * pi / 180 # in radians
        # bring center of mouse's circle to coordinates 0,0
        x_coord = self.position.x - self.statueObj.position.x
        y_coord = self.position.y - self.statueObj.position.y
        # calculate new position given the change in angle
        x_new = x_coord * math.cos(angle_change) - y_coord * math.sin(angle_change)
        y_new = x_coord * math.sin(angle_change) + y_coord * math.cos(angle_change)
        # bring the center of the mouse's circle to the statue's center, create vector
        new_position = Vector(self.statueObj.position.x + x_new, self.statueObj.position.y + y_new)
        self.position = new_position
        self.heading = self.heading % 360 # do mod 360 so that angle always stay under 360
        return self.position, self.heading

    def reset(self):
        """Resets the mouse to its original heading and position."""
        self.heading = self.originalHeading
        self.position = self.originalPosition