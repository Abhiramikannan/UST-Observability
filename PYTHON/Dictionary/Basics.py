dict1={"brand":"samsung",
        "colours":["red","green"], #values can be any type=here list
        "model":"s23"}
print(dict1)
print(len(dict1))
print(type(dict1))
#dict()method = To make dictionary
dict2=dict(name="abhi",age=23) #no quotes and :
print(dict2)
#access item
x=dict2["name"]
print(x)
#get() method -access
y=dict2.get("name")
print(y)
#key() method - returns all keys in that dictionary
z=dict2.keys()
print(z)
#add item
dict2["job"]="devops engineer"
print(dict2)
#values() - returns list of values in the dictionary
a=dict2.values()
print(a)
#items() - return each item in the dict as tuple inside the list 
b=dict2.items()
print(b)

#checking a specified key exists or not
if "name" in dict2:
    print("'yes',name is there") #single quotes

#changes values - refering to its key name
dict2["name"]="seetha"
print(dict2)
print(dict2["name"])

#update() - update the items
dict2.update({"age":24})
print(dict2["age"])

# Removing items
#1. pop() - removes item of specified key name
dict2.pop("name")
print(dict2)

#2.popitem() - remove the last inserted one
dict2.popitem()
print(dict2)

#3.del = delete the specified key name , also remove entire dict
del dict1["brand"] #removes key and value of brand
print(dict1)
del dict2 #delte entire dict, also variable =raises error
print(dict2)

#loop through dictionary:
dict3={"name":"ammu","age":40,"marks":50}
for x in dict3:
    print(x) #print all key names in dict

#To print values:
for x in dict3:
    print(dict3[x])
    
#to print key and values
for x in dict3:
    print(x,dict3[x])

#values()=to return all values
for x in dict3.values():
    print(x)

#keys() = to return the keys:
for x in dict3.keys():
    print(x)

#items()=loop through all keys and values
for x,y in dict3.items():
    print(x,y)

#copy dictionary
#1. copy()
mydict1=dict3.copy()
print(mydict1)

#2.dict()
mydict2=dict(mydict1)
print(mydict2)

#nested dictionaries : dictionary contains dictionary
myfamily={
          "child1":{
                  "name":"akash",
                  "age":25
          },
          "child2":{
              "name":"anu",
               "age":30
          },
          "child3":{
              "name":"mamta",
              "age":28
          }
          }
print(myfamily)

#acces item from nested dictionary
print(myfamily["child1"]) #use quotes

