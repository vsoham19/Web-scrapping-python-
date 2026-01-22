a = 33
b = 200
if b > a:
  print("b is greater than a")

#elif
c = 33
d = 33  
if d > c:
    print("d is greater than c")
elif c == d:
    print("c and d are equal")
else:
    print("c is greater than d")

#nested if
x = 41
if x > 10:
    print("x is above 10")
    if x > 20:
        print("x is also above 20")
    else:
        print("x is not above 20")
#and
y = 25  
if y > 10 and y < 30:
    print("y is between 10 and 30") 
#or
z = 15  
if z > 20 or z < 30:
    print("z is either above 20 or below 30")   
#nested if with and/or
m = 50  
if m > 10:
    print("m is above 10")
    if m > 20 and m < 60:
        print("m is between 20 and 60")
    else:
        print("m is not between 20 and 60")

#pass statemets
n = 100
if n > 50:
    pass
    print("n is above 50")
#continue statement
for i in range(10):
    if i == 5:
        continue
    print(i)

#break statement
for j in range(10):
    if j == 5:
        break
    print(j)

#matching statement
day = "Monday"
match day:
    case "Monday":
        print("It's Monday!")
    case "Tuesday":
        print("It's Tuesday!")
    case _:
        print("It's some other day.")