import json 
import csv 

with open("alabama-history.csv","r") as f:
     reader = csv.reader(f)
#      print(reader)
     data = {"names":[]}
     for row in reader:
         data["names"].append({"firstname":row[0],"age":row[1]})
#      print(data)

with open("names.json","w") as f:
     json.dump(data,f,indent=4)
     