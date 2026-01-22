#simple
print("Hello, World!")

#quote inside quotes
print('He said, "Hello!"')

#assign to a variable 
a = "hello"
print(a)

b = """this is a ,
multi-line string
example."""
print(b)

#array
c = "Nirma Uni."
print(c[1])

#loop through a string
d = "banana"
for x in d:
    print(x)

#string length
e = "Highest"
print(len(e))

#check string
f = "Donald is duck"
print("duck" in f)
print("fuck" not in f)

#slicing
g = "Python is simple"
print(g[2:5])
#slice from start
print(g[:5])
#slice to end
print(g[5:])

#modify string
h = "Hello, World!"
print(h.upper())
print(h.lower())

#remove whitespace
i = "   Hello, World!   "
print(i.strip())    

#replace string
j = "Hello, World!"     
print(j.replace("H", "J"))

#split string
k = "Hello, World!"
print(k.split(","))

l = "Soham"
m = "Vaghasia"
n = l + " " + m
print(n)

#f-string
age = 25
txt = f"My name is Soham, and I am {age} years old."
print(txt)

