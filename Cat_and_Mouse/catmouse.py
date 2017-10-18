from tkinter import *                  # Import everything from Tkinter
from Arena   import Arena              # Import our Arena
from Turtle  import Turtle             # Import our Turtle
from Vector  import *                  # Import everything from our Vector
from statue import Statue
from mouse import Mouse
from cat import Cat
from statue import scale_factor

# 1 meter = scale_factor pixels, variable located in statue.py

def runGame(catRadius, catAngle, mouseAngle):
	"""
	Main function that organizes and runs the game. Creates statue, mouse, and cat and adds them to the area.
	"""
	tk = Tk()                              # Create a Tk top-level widget
	arena = Arena(tk)                      # Create an Arena widget, arena
	arena.pack()                           # Tell arena to pack itself on screen

	statueObj = Statue(Vector(200,200))	   # Create statue at 200,200
	arena.add(statueObj)				   # Add statue to arena

	mouseObj = Mouse(mouseAngle, statueObj)	# Create mouse with statue passed as argument
	arena.add(mouseObj)						# Add mouse to arena

	cat_radius_scaled = catRadius * scale_factor		# Scale the radius of the cat to pixels
	catObj = Cat(catAngle, cat_radius_scaled, mouseObj)	# Create cat with mouse passed as argument
	arena.add(catObj)									# Add cat to arena

	arena.setLabels() # added (set labels to starting position)
	tk.mainloop()                          # Enter the Tkinter event loop

if __name__ == "__main__":
	# the first argument is the starting angle of the mouse in degrees
	# the second argument is the starting angle of the cat in degrees
	# the third arguemnt is the starting distance from the cat to the center of the statue
	runGame(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))
