list = ["rohit","virat","sachin","dhoni"]
print(list)
list.append("yuvi")
print(list)
print(len(list))

#access items
print(list[3])
print(list[-1])
print(list[1:4]) 

list[0] = "Brohit"
print(list)

#INSERT ITEMS
list.insert(2,"Hardik")
print(list)

aussie = ["Smith","Warner","Maxwell"]
list.extend(aussie)
print(list)

#remove items
list.remove("sachin")
print(list)

#remove from index
list.pop(3)
print(list)
del list[0] #removes the specific index as well
print(list)

list.clear() #clears the entire list
print(list)

#list comprehension
fruits = ["apple","angoor","anaar","bananna","chickoo","dodo"]
a_fruit = []
for x in fruits:
    if "a" in x:
        a_fruit.append(x)
print(a_fruit)

a_fruit.sort()
print(a_fruit)
a_fruit.sort(reverse=True)
print(a_fruit)
 
 #join two lists
list1 = [1,2,3]
list2 = ["a","b","c"]   
list3 = list1 + list2
print(list3)

