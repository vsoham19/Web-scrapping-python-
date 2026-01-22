#arithmatic 
a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%2) #modulus
print(a**2) #exponent
print(a//3) #floor division

#assignment
c = 10
c += 5  
print(c)
c -= 3
print(c)
c *= 2
print(c)
c /= 4
print(c)
c %= 3
print(c)


#comparison
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#logical
print(a > 5 and b < 10)
print(a > 5 or b > 10)
print(not(a > 5 and b < 10))

#bitwise
print(a & b)  # AND
print(a | b)  # OR
print(a ^ b)  # XOR
print(~a)     # NOT
print(a << 1) # Left Shift
print(a >> 1) # Right Shift

#membership
list1 = [1, 2, 3, 4, 5]
print(3 in list1)
print(6 not in list1)

#identity
x = 10
y = 10
print(x is y)
print(x is not y)

#operator precedence
result = a + b * 2
print(result)  # Multiplication first, then addition

