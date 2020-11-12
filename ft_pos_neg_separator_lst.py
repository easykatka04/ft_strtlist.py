def ft_pos_neg_separator_lst(a):
    otr = []
    nool = []
    pol = []
    for i in a:
        if i > 0:
            pol.append(i)
        if i < 0:
            otr.append(i)
        if i == 0:
            nool.append(i)
    a = []
    a.append(otr)
    a.append(nool)
    a.append(pol)
    return a
