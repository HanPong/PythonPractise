from tkinter import *

class WidgetsDemoRepeat:
    def __init__(self):
        window=Tk()#creat a window
        window.title("Widgets Demo 2")#set a title

        #Add a check button,and a ratio button to frame1
        #frame是包含其他构件的一个容器构件
        frame1=Frame(window)
        frame1.pack()#creat and add a frame to the window
        self.v1=IntVar()
        cbtBold=Checkbutton(frame1,text="Bold",variable=self.v1,command=self.processCheckbutton)
        self.v2=IntVar()
        rbRed=Radiobutton(frame1,text="Red",bg="red",variable=self.v2,value=1,command=self.processRatiobutton)
        rbYellow=Radiobutton(frame1,text="Yellow",bg="yellow",variable=self.v2,value=2,command=self.processRatiobutton)
        cbtBold.grid(row=1,column=1)
        rbRed.grid(row=1,column=2)
        rbYellow.grid(row=1,column=3)


        #Add a label,an entry,a button,a message to frame2
        frame2=Frame(window)
        frame2.pack()
        label=Label(frame2,text="Enter your name:")
        self.name=StringVar()
        entryName=Entry(frame2,textvariable=self.name)
        btGetname=Button(frame2,text="Get Name",command=self.processButton)
        message=Message(frame2,text="It is a widgets demo.")

        label.grid(row=1,column=1)
        entryName.grid(row=1,column=2)
        btGetname.grid(row=1,column=3)
        message.grid(row=1,column=4)

        #Add text
        text=Text(window)#Create and add text to the window
        text.pack()
        text.insert(END,"Tip\nThe best way to learn Tkinter is to read ")
        text.insert(END,"these carefully designed examples and use them ")
        text.insert(END,"to create your applications")

        window.mainloop()

    def processCheckbutton(self):
        print("check button is"+("checked"if self.v1.get()==1 else "unchecked"))
    def processRatiobutton(self):
        print(("Red"if self.v2.get()==1 else"Yelow")+"is selected.")
    def processButton(self):
        print("Your name is "+self.name.get())

WidgetsDemoRepeat()