import math

class Circle:
    def __init__(self, radius=1):#初始化对象的函数，一开始的这个对象叫做self
        self.radius=radius

    def getPerimeter(self):#求名叫self的圆的周长
        return 2*self.radius*math.pi

    def getArea(self):
        return self.radius*self.radius*math.pi

    def setRadius(self,radius):
        self.radius=radius