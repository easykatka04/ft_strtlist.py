def ft_len(a):
    b = 0
    for i in a:
        b += 1
    return b


def ft_join(a, b):
    c = ""
    d = 0
    if b == "":
        b = " "
    while d != ft_len(a):
        c += str(a[d]) + b
        d += 1
    return c
