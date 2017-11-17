if True:
    print("It's true")

if False:
    print("It's false")

if bool("eggs"):
    print("Yes please bool")

if "eggs":
    print("Yes please string")

#Else keyword
n = 42
if n > 50:
    print("Greater than 50")
else:
    print("50 or smaller")

#Nested if else statement
#Zen of Python: Flat is better than nested, use elif instead of nested if and else
if n > 50:
    print("Greater than 50")
elif n == 32:
    print("32")
else:
    print("50 or smaller")
