def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner("Norwegian Blue")
banner("Sun,Moon", "*")
banner(border="*", message="MNNNs")
banner("MNNNs", border="*")

import time
print(time.ctime())


def show_default(arg=time.ctime()):
    print(arg)


show_default()
show_default()
#default argument values are evaluated when def is evaluated.
#They can be modified like any other object


def add_spam(menu=[]):
    menu.append("spam")
    return menu


breakfast = ["egg", "bacon"]
add_spam(breakfast)
print(breakfast)

print(add_spam())
print(add_spam())
print(add_spam())


def add_spam2(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu


print(add_spam())
print(add_spam())
print(add_spam())
