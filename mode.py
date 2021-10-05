import csv
from collections import Counter
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

data = Counter(newdata)
#print(data)

modeDataRange = {
                        "50-60": 0,
                        "60-70": 0,
                        "70-80": 0
                    }

for height , occurence in data.items():
    if 50 < float(height)  < 60:
        modeDataRange["50-60"] += occurence
    elif 60 < float(height)  < 70:
        modeDataRange["60-70"] += occurence
    elif 70 < float(height)  < 80:
        modeDataRange["70-80"] += occurence 

modeRange , modeocc = 0,0
for range, occurence in modeDataRange.items():
    if occurence > modeocc:
        modeRange ,modeocc = [ int(range.split("-")[0]) ,  int(range.split("-")[1]), ]    , occurence

mode = float((modeRange[0]  +  modeRange[1])/2)
#print(mode)
print(f"Mode is -> {mode:2f}")