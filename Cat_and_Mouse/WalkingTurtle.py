from Turtle import Turtle
from Vector import *
from Color import *

class WalkingTurtle(Turtle):       #### Inherit behavior from Turtle
    """This turtle walks in a straight line forever."""

    def __init__(self, position, heading, speed, arena,fill=blue, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.speed = speed
        self.arena = arena
    def getshape(self):
        """Return a list of vectors giving the polygon for this turtle."""
        forward = unit(self.heading)
        right = unit(self.heading + 90)
        return [self.position + forward*30,
                self.position - forward*15 - right*15,
                self.position - forward*15 + right*15]

    def getnextstate(self):
        """Advance straight ahead."""
        # if self.speed >= 20:
        #     self.arena.stop()
        # self.speed += 0.5
        return self.position + unit(self.heading)*self.speed, self.heading
