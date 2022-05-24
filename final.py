import csv
dataset_1=[]
dataset_2=[]

with open("dataset_1.csv","r") as f:
    csvreader= csv.reader(f)
    print(f)
    #print(csvreader)
    for i in csvreader:
        dataset_1.append(i)

with open("datasorted.csv","r") as f:
    csvreader= csv.reader(f)
    print(f)
    #print(csvreader)
    for i in csvreader:
        dataset_2.append(i)        
header1=dataset_1[0]
planet_data1=dataset_1[1:]

header2=dataset_2[0]
planet_data2=dataset_2[1:]

header=header1+header2
#print(header)

planet_data=[]
for index,item in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

with open("final.csv","a+",newline="")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(planet_data)