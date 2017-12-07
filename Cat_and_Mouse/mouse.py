from Turtle import Turtle
from math import cos, sin, pi
from Vector import *
from Color import *
from statue import *

class Mouse(Turtle):
    """ mouse runs around the statue"""
    def __init__(self, heading, statueObj, fill = blue):
        angle = pi * heading / 180
        #Initial mouse position
        self.heading = heading
        position = statueObj.position + Vector(scalar * cos(angle), scalar * sin(angle))
        # self.position = position #REVISION
        self.originalPosition = position
        self.originalHeading = heading
        Turtle.__init__(self, position, heading, fill=fill)
        self.statueObj =statueObj

    def getnextstate(self):
        """Determine a mouse's next state"""
        """
            rotate a degree conterclockwisely
            math formula: x' = x*cos(a) - _y*sin(a)
                          y' = y*cos(a) +  x*sin(a)
        """
        #1s = 1 frame
        # move 1 m in 60s
        # 1 *( 180 /pi) /60 = 3 /pi, which is in degree
        # it moves 3/pi degree per second
        set_angle = 3/pi
        self.heading -= set_angle
        angle = - set_angle * pi / 180 # clockwisely

        # self.heading = 180 - self.heading
        # set_angle = 3/pi
        # self.heading += set_angle
        # angle =  set_angle * pi / 180 #conterclockwisely
        # Set mouse coordinate
        old_x = self.position.x - self.statueObj.position.x
        old_y = self.position.y - self.statueObj.position.y

        new_x = old_x * cos(angle) - old_y * sin(angle)
        new_y = old_y * cos(angle) + old_x * sin(angle)

        new_position = self.statueObj.position + Vector(new_x, new_y)
        self.position = new_position
        self.heading = self.heading % 360
        return self.position, self.heading
    def reset(self):
        self.heading = self.originalHeading
        self.position = self.originalPosition
