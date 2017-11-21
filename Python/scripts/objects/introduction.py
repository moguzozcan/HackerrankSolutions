x = 1000
print(x)

x = 500
print(x)

y = x
print(y)

x = 3000
print(x)
print(y) #y is still 500 since it refers to the memory location, not x

a = 496
print(id(a))

b = 231
print(id(b))

b = a
print(id(b))

print(id(a) == id(b))

#id() deals with the object, not the reference
r = [1,2,3]
print("id of r: " + str(id(r)))

s = r
print("id of s: " + str(id(s)))

s[1] = 12

print(s)
print(r)

print("id of r: " + str(id(r)))

#Value equality vs. identity
#Value - equivalent "contents"
#Identity - same object

