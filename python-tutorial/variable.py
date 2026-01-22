#variable is used to store values 
x = 10
y = "john"
print(x)
print(y)
print(x,y)
#casting is used to specify the datatype of a variable
a = int(3)
b = str(3)
c = float(3)
print(a); print(b); print(c)

#how to know the variable type
print(type(x))
print(type(y))

#Rules for Python variables:

#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#A variable name cannot be any of the Python keywords.

#camel case - each word, except the first, starts with a capital letter
myVariableName = "John"
#pascal case - each word starts with a capital letter
MyVariableName = "John"
#snake case - each word is separated by an underscore _
my_variable_name = "John"

s = "simple"

def fun():
    print("Python is " + s)

fun()