import csv

with open("height-weight.csv",newline='') as f:
    reader = csv.reader(f)
    fdata=list(reader) 
    
#print(fdata)
fdata.pop(0)
#print(fdata)

newdata = []
for i in range(len(fdata)):
    num = fdata[i][1]
    newdata.append(float(num))

#print(newdata)

n = len(newdata)
sum = 0
for x in newdata:
    sum +=x

mean = sum/n

#print('\n mean of the data is this =  ' + str(mean))

print(f"mean is this  =  {mean}")

