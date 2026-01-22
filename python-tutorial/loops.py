#while loop
i = 1
while i <= 7:
    #print("Iteration:", i)
    i += 1

#break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#continue
i = 1
while i < 6:
    i += 1
    
    if i == 3:
        continue  
    print(i)

#nested while loop
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print("i =", i, "j =", j)
        j += 1
    i += 1


#for loops

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)    

#break
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break
#continue
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
#nested for loop
colors = ["red", "yellow", "green"]
for fruit in fruits:
    for color in colors:
        print(fruit, "is", color)
#loop through a string
for letter in "banana":
    print(letter)
#range functiom

for i in range(6):
    print(i)
for i in range(2, 6):
    print(i)
