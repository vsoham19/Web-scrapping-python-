set1 = {"anu", "banu", "canu"}

#set are unordered and immutable
#set does not allow duplicate values
#length of set
print(len(set1))
print(type(set1))
#set can be made using a construcor 
thisset = set(("apple", "banana", "cherry"))
print(thisset)

#access items using for loop
for items in set1:
    print(items)

print("canu" in set1)

#once set is created you cannot change items but add new items 
set1.add("danu")
print(set1)

#adding another set
set2 = {"eanu", "fanu"}
set1.update(set2)   
print(set1)
#to remove a set item
set1.remove("banu")
#you can also use discard method in place of remove uf the item in remove does not exist it will raise an error but in discard it will not raise the error 
#there is also a pop method which can remove a random item


#union of two sets
set3 = {"xanu", "yanu"}
set4 = set1.union(set3)
print(set4)
#we can also use | operator for union
#set5 = set1 | set3

#uodate
set1.update(set3)
print(set1)

#intersection of two sets
set5 = set1.intersection(set3)
print(set5)
#we can also use & operator for intersection
#set6 = set1 & set3
#symmetric difference
set6 = set1.symmetric_difference(set3)
print(set6)
#we can also use ^ operator for symmetric difference
#set7 = set1 ^ set3

#difference
set7 = set1.difference(set3)
print(set7)
#print(set1 - set3)
#we can also use - operator for difference
#set8 = set1 - set3

