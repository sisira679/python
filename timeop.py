class Time:
    def __init__(self,hour,minute,second):
       self.__hour=hour
       self.__minute=minute
       self.__second=second

    def __add__(self, other):
        return 'time is :'+ str(self.__hour+ other .__hour)+':'+str(self.__minute+other .__minute)+':'+str(self.__second+other.__second)
    def __lt__(self, other):
        if(self. __hour<other.__hour):
            return ("true")
        elif(self.__hour==other.__hour):
            if(self.__minute<other.__minute):
                return ("true")
            elif(self.__minute==other.__minute):
                    if (self.__second< other.__second):
                        return ("true")
                    else:
                        return("false")
        else:
            return("false")


h=int(input ("enter the hour:"))
m=int(input("enter the minute"))
s=int(input("enter the second"))
h1= int(input("enter the hour:"))
m1= int(input("enter the minute"))
s1= int(input("enter the second"))
t1=Time(h,m,s)
t2=Time(h1,m1,s1)
print(t1+t2)
print(t1<t2)
