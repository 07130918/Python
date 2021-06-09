def outer(a1, a2):

    def inner(a3, a4):
        return a3 / a4

    r1 = inner(a1, a2)
    r2 = inner(a2, a1)
    print(r1, r2, r1 + r2)


outer(8, 4)
