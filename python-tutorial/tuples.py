my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
print(len(my_tuple))

# TO CREATE TUPLE WITH ONE ITEM
tuple1 = ("soham",)
print(type(tuple1))

# it can be also made using a constructor 
tuple2 = tuple(("cabbage","tomato","potato"))
print(tuple2)

# access items using index and negative index
print(my_tuple[1])
print(my_tuple[-2])
print(my_tuple[0:2]) #slicing

# to change the values of the tuple first you need to convert the tuple into a list
x = (10,20,30)
print(x)
y = list(x)
y[1] = 25
x = tuple(y)
print(x)

#same procedure to remove the element
z = list(x)
z.remove(30)    
x = tuple(z)
print(x)

#for loop through a tuple
for item in my_tuple:
    print(item) 
#check if item exists
if "banana" in my_tuple:
    print("Yes, banana is present") 
#join two tuples
tuple3 = ("orange","grape") 
tuple4 = my_tuple + tuple3
print(tuple4)

#while loops
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1  

#tuple join same as lists
