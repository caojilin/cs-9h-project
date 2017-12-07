# from tkinter import *
# Button(text="L").pack (side=LEFT,   expand=YES, fill=BOTH)
# Button(text="T").pack (side=TOP,    expand=YES, fill=BOTH)
# Button(text="R").pack (side=RIGHT,  expand=YES, fill=BOTH)
# Button(text="B").pack (side=BOTTOM, expand=YES, fill=BOTH)
# # Button(text="LL").pack(side=LEFT,   expand=YES, fill=BOTH)
# # Button(text="TT").pack(side=TOP,    expand=YES, fill=BOTH)
# mainloop()

from tkinter import *

def on_win_request(parent):
    dialog = Toplevel(width=400,height=300)
    parent.wait_window(dialog)
    # executed only when "dialog" is destroyed
    print("Mini-event loop finished!")

def aboutMenu():
    top = Toplevel(width=400,height=300)
    top.title("About this application...")

    msg = Message(top, text="about_message")
    msg.pack()

    button = Button(top, text="Dismiss", command=top.destroy)
    button.pack()
r = Tk()
f = Frame(r)
f.config(width=400,height=300)
# b = Button(r, text='New Window', command=lambda: on_win_request(r))
# b.pack(anchor=NW)
# Label(r,text='This is a label').pack(anchor=NW)
# time = StringVar()
# time1= 1
# label = Label(f, textvariable=time)
# label.pack()
# def add(time1):
#     time1 += 1
#     time.set(str(time1))
# time.set('1')
# Button(f,text='click me', command=add(time1)).pack()
# b3 = Button(r, text ='About', command = aboutMenu)
# b3.pack(anchor=NW)
f.pack()


r.mainloop()
