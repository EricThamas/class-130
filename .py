# array=[[1,2,3,4,5],[10,20,30,40]]
# print(array[-2:])

# x=lambda a,b:a**b
# print(x(9,3))

#students_tuples=[
    #('john',"A",15),
    #("jane","B",12),
    #("dave","C",10),
#]
#data=sorted(students_tuples,key=lambda a:a[2])
#print(data)

import csv
data=[]

with open("dataset_2.csv","r") as f:
    csvreader= csv.reader(f)
    print(f)
    #print(csvreader)
    for i in csvreader:
        data.append(i)
        #print(data)
headers=data[0]
print(headers)

planet_data=data[1:]
print(planet_data)

for i in planet_data:
    i[2]= i[2].lower()
planet_data.sort(key=lambda a:a[2])

with open("datasorted.csv","a+",newline="")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)