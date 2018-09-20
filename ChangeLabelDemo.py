from tkinter import *
class ChangeLabelDemo:
    def __init__(self):
        window=Tk()#Create a window
        window.title("Change Label Demo")

        #Add a label to frame1
        frame1=Frame(window)
        frame1.pack()
        self.lbl=Label(frame1,text="Programming is fun")
        self.lbl.pack()

        #Add a label,entry,button,and two radio buttons to frame2
        frame2=Frame(window)
        frame2.pack()
        label=Label(frame2,text="Enter text:")
        self.msg=StringVar()
        entry=Entry(frame2,textvariable=self.msg)
