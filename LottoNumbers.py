#编写一个程序决定输入的数字是否涵盖了1到99之间的数
isCovered=99*[False]#创建了99个初始化为false的布尔类型列表
endOfInput=False
while not endOfInput:
    #Read numbers as a string from the console
    s=input("Enter a line of numbers separated by spaces: ")
    items=s.split()#把字符串s按照空格分开
    lst=[eval(x)for x in items]#将item中的元素转换成数字并储存在1st数组中

    for number in lst:
        if number==0:
            endOfInput=True
        else:
            isCovered[number-1]=True#如果这个数字为0，则endOfInput为True，如果这个数字不为0，则设置isCovered对应的值为True

#check whether all numbers is covered
allCovered=True
for i in range(99):
    if not isCovered[i]:
        allCovered=False
        break

if allCovered:
    print("The tickets cover all numbers")
else:
    print("The tickets don't cover all numbers")