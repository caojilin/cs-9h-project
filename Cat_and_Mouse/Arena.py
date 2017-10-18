from tkinter import *
from math import sin, cos, pi, sqrt, acos, asin
from Vector import *
from statue import scale_factor
import sys
# from tkColorChooser import askcolor

class Arena(Frame):
    """This class provides the user interface for an arena of turtles."""

    def __init__(self, parent, width=600, height=600, **options):
        Frame.__init__(self, parent, **options)

        # being added section
        mbutton = Menubutton(self, text='File') # create File button
        picks   = Menu(mbutton) # create Menu
        mbutton.config(menu=picks) # add File button to Menu
        picks.add_command(label='About', command=self.aboutMenu) # add About button to File
        picks.add_command(label='Quit', command=sys.exit) # add Quit button to File
        mbutton.pack(anchor=NW)
        mbutton.config(bg='white', bd=4, relief=RAISED)

        self.time = 0 # create integer timer
        self.timeVar = StringVar() # create timer display variable (automatically updates widget)
        self.timeVar.set("Time: "+str(self.time))  # set timer to 0
        Label(self, textvariable=self.timeVar).pack(anchor=NW)

        self.catRadiusVar = StringVar() # create cat radius display variable
        self.catRadiusVar.set("Cat Radius: 0") # set to 0 initially
        Label(self, textvariable=self.catRadiusVar).pack(anchor=NW)

        self.catAngleVar = StringVar() # create cat angle display variable
        self.catAngleVar.set("Cat Angle: 0") # set to 0 initially
        Label(self, textvariable=self.catAngleVar).pack(anchor=NW)

        self.mouseAngleVar = StringVar() # create mouse angle display variable
        self.mouseAngleVar.set("Mouse Angle: 0") # set to 0 initially
        Label(self, textvariable=self.mouseAngleVar).pack(anchor=NW)
        # end added section

        self.width, self.height = width, height
        self.canvas = Canvas(self, width=width, height=height)
        self.canvas.pack()
        parent.title("UC Berkeley CS9H Turtle Arena")
        Button(self, text='reset', command=self.reset).pack(side=LEFT) # added (reset button)
        Button(self, text='step', command=self.step).pack(side=LEFT)
        Button(self, text='run', command=self.run).pack(side=LEFT)
        Button(self, text='stop', command=self.stop).pack(side=LEFT)
        Button(self, text='quit', command=parent.quit).pack(side=LEFT)
        Button(self, text='mouse color', command=self.mouseColorChoose).pack(anchor=SE) # added (mouse color button)
        Button(self, text='cat color', command=self.catColorChoose).pack(anchor=SE) # added (cat color button)
        self.turtles = []
        self.items = {}
        self.running = 0
        self.period = 10 # milliseconds
        self.canvas.bind('<ButtonPress>', self.press)
        self.canvas.bind('<Motion>', self.motion)
        self.canvas.bind('<ButtonRelease>', self.release)
        self.dragging = None

    def hoverEvent(self, event):
        """
        Changes cat color to black when mouse hovers over it.
        This function is called from the motion event handler,
        changes the color when the mouse is located between boundary
        coordinates of cat object.
        """
        marked = False
        for v1 in self.turtles[2].getshape():
            x = v1.x
            y = v1.y
            for v2 in self.turtles[2].getshape():
                x2 = v2.x
                y2 = v2.y
                bool1 = x < event.x and event.x < x2
                bool2 = x > event.x and event.x > x2
                bool3 = y < event.y and event.y < y2
                bool4 = y > event.y and event.y > y2
                if (bool1 and bool3) or (bool2 and bool4) or (bool1 and bool4) or (bool2 and bool3):
                    self.turtles[2].style['fill'] = '#000000' # change color to black
                    self.update(self.turtles[2])
                    marked = True
                    break
        if not marked:
            self.turtles[2].style['fill'] = self.turtles[2].color # set color back to color before hovering
        self.update(self.turtles[2])

    def catColorChoose(self):
        """Button to choose cat color."""
        result = askcolor(color='#F5F5F5', title='Choose the Cat Color') # pop up color picker window
        self.turtles[2].style['fill'] = result[1] # pull out hex color, set it to cat fill
        self.turtles[2].color = result[1] # save color as cat local variable
        self.update(self.turtles[2])

    def mouseColorChoose(self):
        """Button to choose mouse color."""
        result = askcolor(color='#F5F5F5', title='Choose the Mouse Color') # pop up color picker window
        self.turtles[1].style['fill'] = result[1] # pull out hex color, set it to mouse fill
        self.update(self.turtles[1])

    def aboutMenu(self):
        """Creates a popup about window with info and picture."""
        win = Toplevel() # create new Toplevel window
        win.config(width=350, height=150) # set size of window
        win.title('About CS9H Turtle Arena') # set title
        Label(win,  text='CS9H Project 5, Turtle Arena').pack() # add label
        Label(win, text='by Zack Mayeda').pack() # add more info
        Button(win, text='OK', command=win.destroy).pack() # add button to close window
        pic = PhotoImage(file="bridge.gif") # create photo widget
        Button(win, image=pic).pack() # add photo
        win.focus_set()          # take over input focus
        win.grab_set()           # disable other windows while open
        win.wait_window()        # wait here until win destroyed

    def reset(self):
        """Stops the simulation if it's running, and resets the objects to their original values."""
        if self.running == 1:
            self.stop()
        self.turtles[1].style['fill'] = self.turtles[1].originalColor # set mouse back to original color
        self.turtles[2].style['fill'] = self.turtles[2].originalColor # set cat back to original color
        for turtle in self.turtles:
            turtle.reset() # reset turtles to original position and heading using built in functions
            self.update(turtle)
        self.time = 0

    def press(self, event):
        dragstart = Vector(event.x, event.y)
        for turtle in self.turtles:
            if (dragstart - turtle.position).length() < 10:
                self.dragging = turtle
                self.dragstart = dragstart
                self.start = turtle.position
                return

    def motion(self, event):
        self.hoverEvent(event) # added (call hoverEvent function that changes color to black)
        drag = Vector(event.x, event.y)
        if self.dragging:
            self.dragging.position = self.start + drag - self.dragstart
            self.dragCat(self.dragging.position) # added (call dragCat function that updates cat position and heading)
            self.update(self.dragging)

    def dragCat(self, dragPosition):
        """Update the cat's radius and angle when dragged."""
        newRadius = sqrt( (200 - dragPosition.x) ** 2 + (200 - dragPosition.y) ** 2) # calculate new radius of cat from center of statue
        newAngle = acos(abs(200 - dragPosition.x)/newRadius) # calculate new angle using @ = arc cos (x / r), more calc below
        newAngle *= 180/pi # convert to degrees
        x_coord = dragPosition.x - 200
        y_coord = dragPosition.y - 200
        # correct angle for each quadrant
        # quad IV
        if x_coord > 0 and y_coord > 0:
            newAngle = newAngle
        # quad III
        if x_coord < 0 and y_coord > 0:
            newAngle = 180 - newAngle
        # quad II
        if x_coord < 0 and y_coord < 0:
            newAngle += 180
            newAngle = newAngle
        # quad I
        if x_coord > 0 and y_coord < 0:
            newAngle = 360 - newAngle
        self.turtles[2].heading = newAngle # update cat heading
        if newRadius < scale_factor: # prevent cat radius from being less than statue radius
            newRadius = scale_factor
            newX = 200 + newRadius * cos(pi/180 * newAngle)
            newY = 200 + newRadius * sin(pi/180 * newAngle)
            newPosition = Vector(newX, newY)
            self.turtles[2].position = newPosition
        self.turtles[2].radius = newRadius # update cat radius
        self.setLabels()

    def release(self, event):
        self.dragging = None

    def update(self, turtle):
        """Update the drawing of a turtle according to the turtle object."""
        item = self.items[turtle]
        vertices = [(v.x, v.y) for v in turtle.getshape()]
        self.canvas.coords(item, sum(vertices, ()))
        self.canvas.itemconfigure(item, **turtle.style)

    def add(self, turtle):
        """Add a new turtle to this arena."""
        self.turtles.append(turtle)
        self.items[turtle] = self.canvas.create_polygon(0, 0)
        self.update(turtle)

    def step(self, stop=1):
        """Advance all the turtles one step."""
        nextstates = {}
        for turtle in self.turtles:
            nextstates[turtle] = turtle.getnextstate()
        for turtle in self.turtles:
            turtle.setstate(nextstates[turtle])
            self.update(turtle)
        if stop:
            self.running = 0
        # added section
        self.time += 1 # increase integer timer
        self.timeVar.set("Time: "+str(self.time/60)) # update timer display variable
        self.setLabels() # update all angles, radius

    def setLabels(self):
        """Update the cat radius, cat angle, and mouse angle labels."""
        mouseAngle = self.turtles[1].heading
        catAngle = self.turtles[2].heading
        catRadius = self.turtles[2].radius
        self.mouseAngleVar.set("Mouse Angle: " + str(int(mouseAngle)))
        self.catAngleVar.set("Cat Angle: " + str(round(catAngle,3)))
        self.catRadiusVar.set("Cat Radius: " + str(round(catRadius/scale_factor,3)))

    def run(self):
        """Start the turtles running."""
        self.running = 1
        self.loop()

    def loop(self):
        """Repeatedly advance all the turtles one step."""
        self.step(0)
        if self.running:
            self.tk.createtimerhandler(self.period, self.loop)

    def stop(self):
        """Stop the running turtles."""
        self.running = 0
