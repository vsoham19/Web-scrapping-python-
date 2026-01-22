def my_fun():
    x = 10
    y = 20
    print(x + y)
    return x + y
    
my_fun()

def farhan_to_celsius(farhan):
    celsius = (farhan- 32) * 5/9
    return celsius
temp = farhan_to_celsius(100)
print("Temperature in celsius is:", temp)


#function argument 
def greet(name,lastname):
    print("Good morning ", name, lastname)
greet("Soham","Sharma")

#*args
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
#**kwargs
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

