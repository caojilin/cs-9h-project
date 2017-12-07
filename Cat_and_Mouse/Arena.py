from tkinter import *
from math import sin, cos, pi, sqrt, acos, asin
from statue import *
from Vector import *
import sys

class Arena(Frame):
    """This class provides the user interface for an arena of turtles."""

    def __init__(self, parent, width=700, height=700, **options):
        Frame.__init__(self, parent, **options)
        #added section
        mybutton = Menubutton(self, text ="File") #File Button
        picks = Menu(mybutton)#create menu
        mybutton.config(menu=picks) #add File button to Menu
        picks.add_command(label ="About", command =self.aboutMenu) # add About button to File
        picks.add_command(label ="Quit", command = sys.exit) #add quit button to File
        mybutton.pack(anchor = NW) #anchored at North West
        mybutton.config(bg='white', bd=4, relief=RAISED )
        #added end

        #add variable information
        self.time = 0 # integer timer
        self.timeVar = StringVar()
        self.timeVar.set('Time:' + str(self.time))
        Label(self, textvariable = self.timeVar).pack(anchor =NW)

        self.catRadiusVar = StringVar()
        self.catRadiusVar.set('Cat radius: 0') #initially 0 set
        Label(self,textvariable=self.catRadiusVar).pack(anchor=NW)

        self.catAngleVar = StringVar()
        self.catAngleVar.set('Cat angle: 0')
        Label(self, textvariable = self.catAngleVar).pack(anchor = NW)

        self.mouseAngleVar = StringVar()
        self.mouseAngleVar.set('Mouse angle: 0')
        Label(self, textvariable= self.mouseAngleVar).pack(anchor =NW)

        #enned variable information

        self.width, self.height = width, height
        self.canvas = Canvas(self, width=width, height=height)
        self.canvas.pack()
        parent.title("UC Bereley CS9H Turtle Arena")
        Button(self, text='step', command=self.step).pack(side=LEFT)
        Button(self, text='run', command=self.run).pack(side=LEFT)
        Button(self, text='stop', command=self.stop).pack(side=LEFT)
        Button(self, text='reset', command=self.reset).pack(side=LEFT)
        Button(self, text='quit', command=parent.quit).pack(side=LEFT)

        Button(self, text ='=', command =self.set_radius).pack(side=RIGHT)
        self.entry1 = Entry(self)
        self.entry1.pack(side=RIGHT)
        Label(self,text='cat radius', ).pack(side=RIGHT)

        self.turtles = []
        self.items = {}
        self.running = 0
        self.period = 10 # milliseconds
        self.canvas.bind('<ButtonPress>', self.press)
        self.canvas.bind('<Motion>', self.motion)
        self.canvas.bind('<ButtonRelease>', self.release)
        self.dragging = None

    def set_radius(self):
        num = scalar * float(self.entry1.get())
        the_cat = self.turtles[2]
        the_cat.radius = num
        the_cat.position = the_cat.statueObj.position + Vector(the_cat.radius*cos(pi*the_cat.heading /180), the_cat.radius*sin(pi*the_cat.heading /180))
        self.update(self.turtles[2])
        # self.stop()

    def aboutMenu(self):
        """Creates a popup about window with info"""
        window = Toplevel() #create new Toplevel window
        window.config(width = 350, height=150) # size of window
        window.title('About Turtle Arena') # set title
        Label(window, text = 'CS9H Project 5, Turtle Arena').pack() #add Label
        Label(window, text = 'By caojilin').pack()
        Button(window, text='OK', command=window.destroy).pack() #button to close window
        pic = PhotoImage(file="image.png") #create Photo widget
        Button(window, image=pic).pack() # add Photo
        # window.focus_set()  #take over input focus
        # window.grab_set() #disable other window while open
        window.wait_window() #wait here until window destroyed

    #added feature
    def setLabels(self):
        """update cat's radius, angle and mouse angle labels"""
        catRadius = self.turtles[2].radius
        catAngle = self.turtles[2].heading
        mouseAngle = self.turtles[1].heading
        self.catRadiusVar.set('Cat radius:' + str(round(catRadius/scalar, 3)))
        self.catAngleVar.set('Cat angle:'+ str(round(catAngle, 3)))
        self.mouseAngleVar.set('Mouse angle:' + str(int(mouseAngle)))

    def hoverEvent(self, event):
        """
        change cat color to black when mouse hovers over it.

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

    def press(self, event):
        dragstart = Vector(event.x, event.y)
        for turtle in self.turtles:
            if (dragstart - turtle.position).length() < 10:
                self.dragging = turtle
                self.dragstart = dragstart
                self.start = turtle.position
                return

    def dragCat(self, dragPosition):
        """Update the cat's radius and angle when dragged."""
        newRadius = sqrt( (300 - dragPosition.x) ** 2 + (300 - dragPosition.y) ** 2) # calculate new radius of cat from center of statue
        newAngle = acos(abs(300 - dragPosition.x)/newRadius) # calculate new angle using @ = arc cos (x / r), more calc below
        newAngle *= 180/pi # convert to degrees
        x_coord = dragPosition.x - 300
        y_coord = dragPosition.y - 300
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
        if newRadius < scalar: # prevent cat radius from being less than statue radius
            newRadius = scalar
            newX = 300 + newRadius * cos(pi/180 * newAngle)
            newY = 300 + newRadius * sin(pi/180 * newAngle)
            newPosition = Vector(newX, newY)
            self.turtles[2].position = newPosition
        self.turtles[2].radius = newRadius # update cat radius
        self.setLabels()

    def motion(self, event):
        self.hoverEvent(event)
        drag = Vector(event.x, event.y)
        drag = Vector(event.x, event.y)
        if self.dragging:
            self.dragging.position = self.start + drag - self.dragstart
            self.dragCat(self.dragging.position)
            self.update(self.dragging)

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

    def reset(self):
        """stop the simulation if it's running, and resets the objects to their original valuse"""
        self.time=0
        self.timeVar.set('Time: 0')
        self.catRadiusVar.set('Cat radius: 0') #initially 0 set
        self.catAngleVar.set('Cat angle: 0')
        self.mouseAngleVar.set('Mouse angle: 0')
        if self.running ==1:
            self.stop()
        for turtle in self.turtles:
            turtle.reset()
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
        #added part
        self.time += 1
        self.timeVar.set('Time:' + str(round(self.time/60,3)))
        self.setLabels() #update all labels

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
