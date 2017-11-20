def square(x):
    return x * x


print(square(5))


def launch_missiles():
    print("Missiles launched")


launch_missiles()


def even_or_odd(n):
    if n % 2 == 0:
        print("even")
        return
    print("odd")

even_or_odd(3)