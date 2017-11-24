w = "the quick asdfa dog cat line the".split()
print(w)
print(w.index('dog'))
#print(w.index('unicorn'))
print(w.count("the"))
print("the" in w)
print("the" not in w)

u = "jackdows love my big sphinx of quartz".split()
print(u)
del u[3]
print(u)
u.remove('love')
print(u)
del u[u.index('my')]
print(u)

#u.remove('pyramid')

u.insert(2, "oguz")
print(u)
print(' '.join(u))
