dict1 = {"brand": "Ford",
         "model": "Mustang",
         "year": 1964}

#dictionary is used to store data values in key:value pairs
print(dict1)
#length of dictionary
print(len(dict1))
print(type(dict1))

x = dict1["model"]
print(x)

x = dict1.keys()
print(x)
x = dict1.values()
print(x)
#change items
dict1["year"] = 2020
#uodate method
dict1.update({"color": "red"})
print(dict1)
#add items
dict1["price"] = 55000
print(dict1)    
#remvoe items
dict1.pop("model")  
print(dict1)
dict1.popitem() #removes the last inserted item
print(dict1)
#loop through a dictionary
for key in dict1:
    print(key)
#nested dictionaries
child1 = {"name" : "Emil", "year" : 2004}
child2 = {"name" : "Tobias", "year" : 2007}
child3 = {"name" : "Linus", "year" : 2011}
myfamily = {"child1" : child1, "child2" : child2, "child3" : child3}
print(myfamily)
#asses items in nested dictionary
print(myfamily["child2"]["name"])