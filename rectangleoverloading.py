class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
        self.area=length*width
    def __lt__(self,other):
        if self.area<other.area:
            return "Rectangle 1 is smaller in area"
        else:
            return "Rectangle 2 is smaller in area"
r1=Rectangle(50,20)
r2=Rectangle(30,10)
print(r1<r2)

