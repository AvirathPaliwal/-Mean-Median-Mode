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

n = len(newdata)
newdata.sort()

# floor division is shown by //
if n %2 == 0:
    median1 = float( newdata[n//2])
    median2 = float( newdata[n//2-1])
    median = (median1+median2)/2
else:
    median = newdata[n//2]


print('median is this ' + str(median))