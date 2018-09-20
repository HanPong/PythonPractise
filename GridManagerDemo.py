from tkinter import *

class GridManagerDemo:
    window=Tk()
    window.title("Grid Manager Demo")

    message=Message(window,text="This Message weight occupies three rows and two columns")
    message.grid(row=1,column=1,rowspan=3,columnspan=2)
    Label(window,text="First name:").grid(row=1,column=3)
    Entry(window).grid()