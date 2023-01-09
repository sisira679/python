# program to copy odd lines of one file to another.
#opening file for reading and writing data
input_file=open('demo.txt')
output_file=open('WriteData.txt','w')
#coping/reading contents from read_file to copy_data
copy_data = input_file.readlines()
print("\nActual File Content is:")
print(copy_data,"\n")

for i in range(0,len(copy_data)):
    if i % 2==0:
        output_file.write(copy_data[i])
    else:
        pass


#closing file after writing
output_file = open('WriteData.txt','r')
print("Odd Lines are:")
print(output_file.read())

#closing Files
input_file.close()
output_file.close()
