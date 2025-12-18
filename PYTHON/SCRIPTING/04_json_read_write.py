import json
#write json
with open("file1.json","w") as f:
    data=json.dump({
  "title": "Sales Report",
  "year": 2025
},f
)
    #read json
with open("file1.json","r") as f:
    data=json.load(f)
    print("read succesfully")
print(data["title"])
print(data["year"])


#write json to a file
data={"name": "Grafana","type":"dashboard"}
with open("sample.json","w") as f:
    json.dump(data,f)
    print("written succesfully")

#read json from a file
with open("sample.json","r") as f:
    data=json.load(f)
print("read data:" ,data)
