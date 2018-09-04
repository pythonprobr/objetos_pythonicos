a = 5


def f(a=3):
    b = 3
    print(globals())
    print(locals())
    print(a)
    print(b)


class A:
    a = 8
    a += 1
    print(a)
    print(globals())
    print(locals())

# f()
