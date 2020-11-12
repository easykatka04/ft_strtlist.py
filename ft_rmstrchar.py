def ft_rmstrchar(a, b):
    c = ""
    l = 0
    for i in a:
        if i not in b:
            c += i
        if i in b:
            l += 1
    return c
