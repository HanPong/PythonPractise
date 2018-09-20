from Circle import Circle

def main():

    #创建一个半径为1的圆
    circle1=Circle() #初始化的self的圆半径就是1
    print("The area of the circle of radius:",circle1.radius,"is",circle1.getArea())

    circle2=Circle(25)
    print("The area of the circle of radius:", circle2.radius, "is", circle2.getArea())

    circle2.radius=100
    print("The area of the circle of radius:", circle2.radius, "is", circle2.getArea())


main()


