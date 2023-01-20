colour1=input("\nenter the first set colors:").split(",")
colour2=input("\nenter the next set colors:").split(",")
set1=set(colour1)
set2=set(colour2)
x=set1.difference(set2)
y=set2.difference(set1)
mylist=list(x)
mylist1=list(y)
mylist2=mylist1+mylist
print(mylist2)




