 from tkinter import *

window=Tk()#创建一个窗口
label=Label(window,text="Welcome to Python")#创建一个标签，小构建类
button=Button(window,text="Click me")
label.pack()#把标签放进窗口中
button.pack()

window.mainloop()