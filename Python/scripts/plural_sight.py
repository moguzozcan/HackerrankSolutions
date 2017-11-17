import math

x = math.sqrt(81)
print(x)

y = math.factorial(4)
print(y)

from math import factorial
print(factorial(3))

from math import factorial as fac
print(fac(5))

n = 5
k = 3
print(fac(n) / (fac(k) *  fac(n - k)))
print(fac(n) // (fac(k) *  fac(n - k)))

print(2**31 - 1)
print(fac(13))
#Python int limit is limited with memory of the PC

print(fac(100))
print(len(str(fac(100))))

#help(math)

