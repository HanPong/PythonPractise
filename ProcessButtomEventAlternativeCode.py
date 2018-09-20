#这个程序与上一个程序的不同之处是将函数放在了一个类中
from tkinter import *

class ProcessButtonEvent:
    def __init__(self):
        window=Tk()#创建一个窗口
        btOK=Button(window,text="ok",fg="red",command=self.processOK)
        btCancel=Button(window,text="Canel",bg="yellow",command=self.processCanel)

        btOK.pack()
        btCancel.pack()

        window.mainloop()

    def processOK(self):
        print("OK button is clicked.")

    def processCanel(self):
        print("Canel button is clicked.")

ProcessButtonEvent()