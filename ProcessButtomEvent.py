from tkinter import *

def processOK():
    print("OK button is clicked.")

def processCancel():
    print("Cancel button is clicked.")

window=Tk()#创建一个窗口
btOK=Button(window,text="OK",fg="red",command=processOK)#设置一个按钮，并将其宇processOK函数绑定，前景色为红色
btCanel=Button(window,text="Cancel",bg="yellow",command=processCancel)

btOK.pack()
btCanel.pack()

window.mainloop()