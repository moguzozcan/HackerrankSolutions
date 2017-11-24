a = [[1, 2], [3, 4]]

b = a[:]

print(a is b)

print(a == b)

print(a[0] is b[0])

a[0] = [8, 9]

print(a[0] is b[0])

a[1].append(5)
print(b[1])

line = input().split()
#l = line.split()

print(line)

