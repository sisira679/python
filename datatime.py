import time
import datetime
print("current date and time:",datetime.datetime.now())
print("current year:",datetime.date.today().strftime("%y"))
print("month of the year:",datetime.date.today().strftime("%B"))
print("week number of year:",datetime.date.today().strftime("%W"))
print("weekend of the week:",datetime.date.today().strftime("%w"))
print("day of year:",datetime.date.today().strftime("%j"))
print("day of the month:",datetime.date.today().strftime("%d"))
print("day of the week:",datetime.date.today().strftime("%A"))


