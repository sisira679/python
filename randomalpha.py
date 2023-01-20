import random
import string
print("Generate a random color hex:")
print("#{:06x}".format(random.randint(0,0xFFFFFF)))
print("\ngenerate a random alphabetical string:")
max_length=225
s=" "
for i in range(random.randint(1,max_length)):
    s+=random.choice(string.ascii_letters)
print(s)
print("\ngenerate a random value between two integers,inclusive:")
print(random.randint(0,10))
print(random.randint(-7,7))
print(random.randint(1,1))
print("\ngenerate a random multiple of 7 between 0 and 70:")
print(random.randint(0,10)*7)