def ft_len(a):
    b = 0
    for i in a:
        b += 1
    return b


def ft_join(a, b=" "):
    c = ""
    for i in range(ft_len(a) - 1):
        c += str(a[i])
        c += b
    c += str(a[-1])
    return c
