def ft_len(s):
    l = 0
    for i in s:
        l += 1
    return l


def ft_sum_even_lst(a):
    b = 0
    for i in range(ft_len(a) - 1):
        if i % 2 == 0:
            b += a[i]
    return b
