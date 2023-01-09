# Program to read each row from a given csv file and print a list of strings.
import csv
# Open the CSV file
with open('data2.csv', 'r') as file:
 # Create a CSV reader
 reader = csv.reader(file)
 # Iterate over the rows of the CSV file
 for row in reader:
  # Print the row as a list of strings
  print(row)
