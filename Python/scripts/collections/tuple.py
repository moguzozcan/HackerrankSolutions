#immutable sequence of arbitrary objects
t = ("norway", 342.1, 12)

print(t)
print(t[0])
print(len(t))

for item in t:
    print(item)

print(t + (23, 525.123))

print(t * 3)

a = ((2,1), (3,6), (23,2439))

print(a[2][1])

h = (391)

print(type(h))

k = (391,)

print(type(k))

e = ()

print(type(e))

p = 1, 3, 54, 123, 32
print(type(p))


def minmax(items):
    return min(items), max(items)


print(minmax([98, 32, 564, 23, 1]))

lower, upper = minmax([98, 32, 564, 23, 1])
print(lower)
print(upper)

(a, (b, (c, d))) = (4, (3, (2, 1)))
print(a)
print(b)
print(c)
print(d)

a = 'jelly'
b = 'bean'
a, b = b, a

print(a)
print(b)

print(tuple([1, 3, 5, 12]))
print(tuple("Carmichael"))

print(5 in (3, 5, 2))

