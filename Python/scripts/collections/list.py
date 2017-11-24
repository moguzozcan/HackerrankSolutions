#Heterogenous mutable sequence

s = "show how to do something".split()
print(s)

print(s[-3])

print(s[1:4])
print(s[1:-1])
print(s[1:])
print(s[:3])

full_slice = s[:]
print(full_slice is s)
print(full_slice == s)

u = s.copy()
print(u)

v = list(s)
print(v)

