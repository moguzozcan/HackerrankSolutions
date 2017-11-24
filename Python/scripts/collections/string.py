#Homogeneous immutable sequence of Unicode codepoints
print(len("llanageşaweqeasdfa"))

print("New" + "found")

s = "New"
s += "Found"

print(s)

s = ";".join(["#765473", "#13123", "#0234"])
print(s)
print(s.split(";"))

print(''.join(['high', 'wawy,', 'man']))

#The way nay not be obvious at first
#To concatenate Invoke join on empty text Something for nothing

print("unforgettable".partition("forget"))

departure, separator, arrival = "London:Edinburg".partition(':')
print(departure)
print(arrival)

departure, _, arrival = "London:Edinburg".partition(':')
print(_)

print("The age of {0} is {1}".format('Jim', 23))

print("The age of {} is {}".format('Jim', 23))

print("The age of {name} is {age}".format(name = "Jim",
                                          age = 23))

