from Turtle import Turtle
from Vector import *
from Color import *
from statue import scale_factor
import math
import sys

class Cat(Turtle):       #### Inherit behavior from Turtle
    """This cat chases the mouse."""

    def __init__(self, heading, radius, mouseObj, fill=red, **style):
        """Create cat with given heading and radius. Call turtle init function."""
        self.heading = heading
        self.originalHeading = heading
        self.radius = radius
        self.originalRadius = radius
        self.originalColor = fill
        self.color = fill
        position = Vector(200 + radius * math.cos(heading*pi/180), 200 + radius * math.sin(heading*pi/180))
        self.originalPosition = position
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.mouseObj = mouseObj
        self.time = 0 # 1 frame is 1 second

    def getnextstate(self):
        """
        Circle around statue. If mouse is visible, move toward statue center by 1 meter.
        Otherwise circle around at current radius for 1.25 meters.
        """
        see_mouse = self.canSeeMouse() # only check every 60 seconds
        if see_mouse and self.radius != scale_factor:

            #print 'cat can see mouse, reducing radius'
            #print 'cat angle =', self.heading
            #print 'mouse angle =', self.mouseObj.heading
            #print 'old radius =',self.radius/scale_factor,

            self.radius -= scale_factor         # reduce radius by 1 meter
            if self.radius < scale_factor:      # if radius is smaller than statue, increase back to statue's radius
                self.radius = scale_factor
            
            #print 'new radius =',self.radius/scale_factor

            # calculate new coordinates with new radius, but same heading
            new_x = 200 + self.radius * math.cos(self.heading * pi/180)
            new_y = 200 + self.radius * math.sin(self.heading * pi/180)
            new_position = Vector(new_x, new_y)
            # check if cat can catch mouse
            self.catWin(self.heading)
            # set new position and heading
            self.position = new_position
            self.heading = self.heading % 360
            self.time += 1
            return self.position, self.heading
        else:
            angle = 1.25 * scale_factor / self.radius * 180/pi * 1/60 # angle change is distance travelled / radius
            self.catWin(self.heading - angle)           # check if cat can catch
            self.heading -= angle                       # reduce heading by calculated angle
            angle_change = -angle * pi / 180 # angle change in radians
            # bring center of cat's circle to 0,0
            x_coord = self.position.x - 200
            y_coord = self.position.y - 200
            # calculate new coordinates, bring center of cat's circle to center of statue
            x_new = 200 + x_coord * math.cos(angle_change) - y_coord * math.sin(angle_change)
            y_new = 200 + x_coord * math.sin(angle_change) + y_coord * math.cos(angle_change)
            new_position = Vector(x_new, y_new)
            # set new position and heading
            self.position = new_position
            self.heading = self.heading % 360
            self.time += 1
            return self.position, self.heading

    def canSeeMouse(self):
        """
        Checks if mouse is visible by the cat with the following formula:
        cat radius * cos(cat angle - mouse angle) >= 1
        """
        if (self.radius/scale_factor * math.cos(self.heading * pi/180 - self.mouseObj.heading * pi/180)) >= 1.0 and self.time % 60 == 0:
            return True
        else:
            return False

    def catWin(self, new_angle):
        """
        Checks to see if the cat catch the mouse with the following formula:
        cos(B - A) > cos(C - A) and cos(C - B) > cos(C - A)
        where B is the angle of the mouse, A is the angle of the cat before moving and C is the angle
        of the cat after moving.
        """
        A = self.heading * pi/180 # old cat angle
        B = self.mouseObj.heading * pi/180 # mouse angle
        C = new_angle * pi/180 # new cat angle
        angle_bool = math.cos(B - A) > math.cos(C - A) and math.cos(C - B) > math.cos(C - A)
        if self.radius == scale_factor and angle_bool: # possibly need to check if minute has elapsed here
            #print 'the mouse has been eaten!'
            #print 'A =',A * 180/pi
            #print 'B =',B * 180/pi
            #print 'C =',C * 180/pi
            sys.exit(0)

    def reset(self):
        """Resets the cat back to its original heading, position, radius, and color."""
        self.heading = self.originalHeading
        self.radius = self.originalRadius
        self.position = self.originalPosition
        self.color = self.originalColor