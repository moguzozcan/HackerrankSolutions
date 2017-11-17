c = 5
while c != 0:
    print(c)
    c -= 1

c = 5
while c:
    print(c)
    c -= 1

#Zen of Python explicit is better than implicit, use the first one

#Infinite loops, if divisible by 7, exit the loop
while True:
    response = input()
    if int(response) % 7 == 0:
        break
