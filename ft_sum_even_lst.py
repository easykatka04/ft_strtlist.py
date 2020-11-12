def ft_len(s):
    l = 0
    for i in s:
        l += 1
    return l


def ft_sum_even_lst(a):
    b = 0
    for i in range(0, ft_len(a) + 1, 2):
        b += i
    return b
