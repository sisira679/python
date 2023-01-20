n = input("enter the string:").split(' ')
list1 = list(n)

set = set(list1)

newlist = list(set)
for i in newlist:
    count = 0
    for j in list1:
        if i == j:
            count = count + 1
    print("occurance of ", i, count)
