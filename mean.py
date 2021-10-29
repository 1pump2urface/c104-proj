import csv
with open("C:/Users/Administrator/Desktop/Python/c104/SOCR-HeightWeight.csv",newline = "")as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)

newdata=[]
for i in range(len(filedata)):
    number = filedata[i][1]
    newdata.append(float(number))


#getting the mean

n = len(newdata)
total = 0
for x in newdata:
    total=total + x

mean = total/n
print("mean is "+ str(mean))