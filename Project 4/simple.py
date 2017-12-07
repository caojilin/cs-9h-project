from tkinter import *                  # Import everything from Tkinter
from Arena   import Arena              # Import our Arena
from Turtle  import Turtle             # Import our Turtle
from Vector  import *                  # Import everything from our Vector
from WalkingTurtle import WalkingTurtle
from statue import *
from mouse import *
from cat import *
import sys

def rungame(catRadius, catAngle, mouseAngle):
    tk = Tk()                              # Create a Tk top-level widget
    arena = Arena(tk)                      # Create an Arena widget, arena
    arena.pack()                           # Tell arena to pack itself on screen
    # arena.add(Turtle(Vector(200,200), 0))  # Add a very simple, basic turtle
    # arena.add(WalkingTurtle(Vector(300,300), 90, 0.5, arena))
    statue = Statue(Vector(300,300))
    arena.add(statue)
    mouse = Mouse(mouseAngle, statue)
    arena.add(mouse)
    catRadius = catRadius * scalar
    cat = Cat(catAngle, catRadius, mouse, statue, arena)
    arena.add(cat)
    tk.mainloop()                          # Enter the Tkinter event loop

if __name__=="__main__":
    rungame(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
