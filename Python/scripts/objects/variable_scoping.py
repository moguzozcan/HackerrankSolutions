#LEGB = Local, Enclosing, Global, Built-in
count = 0


def show_count():
    print(count)


def set_count(c):
    global count
    count = c


show_count()
set_count(5)
show_count()

#Everyhing in Python is an object including functions and modules