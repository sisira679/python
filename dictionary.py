#write a python program to write a python dictionary to a csv file.
#after writing the CSV file read the CSV file and display the content.


import csv
#Data to be inserted
data=[{'Name' : 'john','Age':25,'country':'United States'},
      {'Name' : 'Mike','Age':32,'country':'Canada'},
      {'Name' : 'Sarah','Age':35,'country':'United Kingdom'}]

#write to csv file
with open('people.csv', 'w') as csvfile:
 headernames = ['Name', 'Age', 'country']
 csvwriter = csv.DictWriter(csvfile, fieldnames=headernames)
 csvwriter.writeheader()
 for row in data:
     csvwriter.writerow(row)


#Read from csv file and print contents
with open('data2.csv','r')as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
      print(row)


