from tkinter import *

class WidgetsDemo:
    def __init__(self):
        window=Tk()#初始化中的两项，创建窗口和为窗口取标题
        window.title("Widgets Demo")

        #Add a check button,and a ratio button to frame1
        frame1=Frame(window)#Create and add a frame to window
        frame1.pack()
        self.v1=IntVar()

        cbtBold=Checkbutton(frame1,text="Bold",variable=self.v1,command=self.processCheckbutton)
        self.v2=IntVar()
        rbred=Radiobutton(frame1,text="Red",bg="red",variable=self.v2,value=1,command=self.processRadiobutton)
        rbyellow=Radiobutton(frame1,text="Yellow",bg="yellow",variable=self.v2,value=2,command=self.processRadiobutton)

        cbtBold.grid(row=1,column=1)
        rbred.grid(row=1,column=2)
        rbyellow.grid(row=1,column=3)

        #Add a label,an entry,a button,and a message to frame1
        frame2=Frame(window)#create and add a frame to window
        frame2.pack()
        label=Label(frame2,text="Enter your name:")
        self.name=StringVar()
        entryName=Entry(frame2,textvariable=self.name)
        btGetName=Button(frame2,text="Get name",command=self.processButton)
        message=Message(frame2,text="It is a widgets demo")

        label.grid(row=1,column=2)
        entryName.grid(row=1,column=2)
        btGetName.grid(row=1,column=3)
        message.grid(row=1,column=4)

        #Add text
        text=Text(window)#create and add text to the window
        text.pack()
        text.insert(END,"Tip\nThe best way to learn Tkinter is to read")
        text.insert(END,"these carefully designed examples and use to them")
        text.insert(END,"to create your applications")

        window.mainloop()

    def processCheckbutton(self):
        print("check button is"+("checked"if self.v1.get()==1 else "unchecked"))

    def processRadiobutton(self):
        print(("Red"if self.v2.get()==1 else "Yellow")+"is selected")

    def processButton(self):
        print("Your name is"+self.name.get())

WidgetsDemo()
