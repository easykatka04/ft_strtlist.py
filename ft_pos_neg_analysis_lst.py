def ft_pos_neg_analysis_lst(a):
    kol_h = 0
    max_h = 0
    min_h = 111111111111111111111111011010101001010101010101010101010
    sum_h = 0
    kol_nh = 0
    max_nh = 0
    min_nh = 0
    sum_nh = 0
    c = 0
    l = 0
    b = 0
    for i in a:
        if i > 0:
            kol_h += 1
            sum_h += i
            if i > max_h:
                max_h = i
            if i < min_h:
                min_h = i
        if i < 0:
            kol_nh += 1
            sum_nh += i
            if i > max_nh:
                max_nh = i
            if i < min_nh:
                min_nh = i
        if i == 0:
            b += 1
    c = sum_h//kol_h
    l = sum_nh//kol_nh
    print("Анализ списка:")
    print("Pol:")
    print("Количество чисел: " + str(kol_h) + ",", end=" ")
    print("Количество чисел: " + str(kol_nh) + ",")
    print("Максимальная цифра: " + str(max_h) + ",", end=" ")
    print("Максимальная цифра: " + str(max_nh) + ",")
    print("Минимальная цифра: " + str(min_h) + ",", end=" ")
    print("Минимальная цифра: " + str(min_nh) + ",")
    print("Сумма чисел: " + str(sum_h) + ",", end=" ")
    print("Сумма чисел: " + str(sum_nh) + ",")
    print("Среднее значение: " + str(c) + ",", end=" ")
    print("Среднее значение: " + str(l) + ",")
    print("")
    print("Количество нулей: " + str(b))
