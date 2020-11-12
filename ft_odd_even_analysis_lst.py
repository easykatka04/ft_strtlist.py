def ft_odd_even_analysis_lst(a):
    kol_h = 0
    max_h = 0
    min_h = 111111111111111111111111011010101001010101010101010101010
    sum_h = 0
    kol_nh = 0
    max_nh = 0
    min_nh = 12229487898748390298784948984939493489839849384983948398493849
    sum_nh = 0
    for i in a:
        if i % 2 == 0:
            kol_h += 1
            sum_h += i
            if i > max_h:
                max_h = i
            if i < min_h:
                min_h = i
        else:
            kol_nh += 1
            sum_nh += i
            if i > max_nh:
                max_nh = i
            if i < min_nh:
                min_nh = i
    print("Анализ списка:")
    print("Количество четных чисел: " + str(kol_h) + ",", end="  ")
    print("Количество нечетных чисел: " + str(kol_nh) + ",")
    print("Максимальная четная цифра: " + str(max_h) + ",", end="  ")
    print("Максимальная нечетная цифра: " + str(max_nh) + ",")
    print("Минимальная четная цифра: " + str(min_h) + ",", end="  ")
    print("Минимальная нечетная цифра: " + str(min_nh) + ",")
    print("Сумма четных чисел: " + str(sum_h) + ",", end="  ")
    print("Сумма нечетных чисел: " + str(sum_nh) + ",")
