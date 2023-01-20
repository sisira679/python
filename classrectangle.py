class Rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
       return 2*(self.breadth*self.length)


l1= float(input("Enter length of Rectangle"))
b1= float(input("Enter breadth of Rectangle"))
l2= float(input("Enter length of Rectangle"))
b2= float(input("Enter length of Rectangle"))
rect1=Rectangle(l1,b1)
rect2=Rectangle(l2,b2)
print("Area of Rectangle 1 is {} and perimeter is {}:".format(rect1.area(),rect1.perimeter()))
print("Area of Rectangle 2 is {} and perimeter is {}:".format(rect2.area(),rect2.perimeter()))
print(rect2.area()>rect2.perimeter())


