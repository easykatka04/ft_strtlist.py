def ft_odd_even_separator_lst(a):
    h = []
    neh = []
    for i in a:
        if i % 2 == 0:
            h.append(i)
        else:
            neh.append(i)
    a = []
    a.append(h)
    a.append(neh)
    return a
