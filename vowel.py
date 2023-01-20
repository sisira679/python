sta=input("enter any statement:")
vowels=['a','e','i','o','u']
list1=[]
for x in sta:
    if(x in vowels and x not in list1):
        list1.append(x)
        print("vowels present in given statement:",list1)