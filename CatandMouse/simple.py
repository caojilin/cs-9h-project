from Tkinter import *                  # Import everything from Tkinter
from Arena   import Arena              # Import our Arena
from Turtle  import Turtle             # Import our Turtle
from Vector  import *                  # Import everything from our Vector
from WalkingTurtle import *
from Color import *
from Cat import *
from Mouse import *
from Statue import *

tk = Tk()
tk.geometry('1000x900+400+200')                              # Create a Tk top-level widget
arena = Arena(tk)                      # Create an Arena widget, arena
arena.pack()
arena.add(Mouse(Vector(400,450), 0, 1))
arena.add(Cat(Vector(800,450), 0, 1))                           # Tell arena to pack itself on screen
arena.add(Statue(Vector(500,450), 0, 1))  # Add a very simple, basic turtle
tk.mainloop()                          # Enter the Tkinter event loop
