from Turtle import Turtle
from math import cos, sin, pi
from Vector import *
from Color import *
from statue import *
from mouse import *

class Cat(Turtle):
    """ a cat with radius and angel"""
    def __init__(self, heading , radius, mouseObj, statueObj, arena, fill = red, **style):
        angle = pi*heading /180
        self.heading = heading
        #Initial position
        self.radius = radius # real raidius
        # radius after scale, which corresponds on the screen
        position = statueObj.position + Vector(radius*cos(angle), radius*sin(angle))
        self.originalRadius=radius
        self.originalHeading=heading
        self.originalPosition = position
        self.originalColor = fill
        self.color = fill
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.mouseObj = mouseObj
        self.statueObj = statueObj
        self.arena = arena
        self.time = 0 # 1 frame is 1s, 60s is one minute

    def getnextstate(self):
        """
        Circle around statue. If mouse is visible, move toward statue center by 1 meter.
        Otherwise circle around at current radius for 1.25 meters.
        """
        if self.canSeeMouse() and self.radius > scalar: # and self.time %60 ==0
            self.radius -= scalar
            if self.radius < scalar:
                self.radius = scalar
            # cat's new position
            new_x = self.radius*cos(pi*self.heading /180)
            new_y = self.radius*sin(pi*self.heading /180)
            new_position = self.statueObj.position + Vector(new_x,new_y)
            #check if cat wins
            self.catWin(self.heading)
            self.position = new_position
            self.heading = self.heading % 360

        else:
            # 1 radius = 180/pi , 1.25/2*pi*raidius
            set_angle = 1.25 * scalar*180/(pi * self.radius) / 60
            self.catWin(self.heading - set_angle)
            self.heading -= set_angle
            angle_change = -set_angle * pi /180 # in radius,conterclockwisely
            # set cat't coordinates regarding to statue's center
            """
                rotate a degree conterclockwisely
                math formula: x' = x*cos(a) - _y*sin(a)
                              y' = y*cos(a) +  x*sin(a)
            """
            old_x = self.position.x - self.statueObj.position.x
            old_y = self.position.y - self.statueObj.position.y

            new_x = old_x * cos(angle_change) - old_y * sin(angle_change)
            new_y = old_y * cos(angle_change) + old_x * sin(angle_change)
            # cat's new position
            new_position = self.statueObj.position + Vector(new_x, new_y)
            self.position = new_position
            self.heading = self.heading % 360
        self.time += 1
        return self.position, self.heading

    def catWin(self, new_angle):
        """
        Checks to see if the cat catch the mouse with the following formula:
        cos(B - A) > cos(C - A) and cos(C - B) > cos(C - A)
        where B is the angle of the mouse, A is the angle of the cat before moving and C is the angle
        of the cat after moving.
        """
        #pi* angle/180 is to convert to radians
        A = self.heading * pi /180
        B = self.mouseObj.heading * pi /180
        C = new_angle * pi/180
        angle_bool = cos(B - A) > cos(C - A) and cos(C - B) > cos(C - A)

        if self.radius == scalar and angle_bool:
            self.arena.stop()

    def canSeeMouse(self):
        """
        Checks if mouse is visible by the cat with the following formula:
        cat radius * cos(cat angle - mouse angle) >= 1
        """
        #cat angle - mouse angle
        angle = (self.heading * pi / 180) - (self.mouseObj.heading * pi /180)

        if self.radius /scalar * cos(angle) >= 1 and self.time %60 == 0:
            return True
        else:
            return False

    def reset(self):
        self.radius = self.originalRadius
        self.heading = self.originalHeading
        self.position = self.originalPosition
