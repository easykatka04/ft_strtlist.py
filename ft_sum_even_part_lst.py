def ft_sum_even_part_lst(a):
    b = 0
    for i in a:
        if i % 2 == 0:
            b += i
    return b
