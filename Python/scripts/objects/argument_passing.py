m = [1, 2, 4]

print("m at before function call = ", m)


def modify(k):
    k.append(12)
    print("k = ", k)


modify(m)

print("m = ", m)

f = [14, 23, 37]
print("f before function call = ", f)


def replace(g):
    g = [12, 13, 14]
    print("g = ", g)


replace(f)
print("f = ", f)

#Pass by Object Reference
#The value of the reference is copied, not the value of the object


def f(d):
    return d


c = [1, 3, 5]
e = f(c)

print(c is e)

