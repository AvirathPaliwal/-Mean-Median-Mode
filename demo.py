import csv
from os import stat
with open('height-weight.csv',newline='') as f:
     reader = csv.reader(f)
     file_data = list(reader)

#print(file_data)

from collections import Counter

#Counter is a sub class in dictionary, using Counter tool you can count key-value pair
newdata = "hiavihowareyouavi"
data = Counter(newdata)
# print(data)
# print("\n")

#return the list with all dictionary keys with values. It returns a tuple of key value pairs
# print(data.items())
# print("\n")

#returns the list of all the values in the dictionary. 
# print(data.values())
# print("\n")



import statistics

l = [8,1,5,7,8,11,45,77]
mean = statistics.mean(l)
print(mean)
print(statistics.mode(l))
print(statistics.median(l))