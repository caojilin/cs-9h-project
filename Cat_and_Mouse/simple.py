from tkinter import *                  # Import everything from Tkinter
from Arena   import Arena              # Import our Arena
from Turtle  import Turtle             # Import our Turtle
from Vector  import *                  # Import everything from our Vector
from WalkingTurtle import WalkingTurtle

tk = Tk()                              # Create a Tk top-level widget
arena = Arena(tk)                      # Create an Arena widget, arena
arena.pack()                           # Tell arena to pack itself on screen
arena.add(WalkingTurtle(Vector(200,200), 0, 1))  # Add a very simple, basic turtle
tk.mainloop()                          # Enter the Tkinter event loop
