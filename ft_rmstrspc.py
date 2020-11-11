def ft_rmstrspc(a):
    b = ""
    for i in a:
        if i != " ":
            b += i
        elif i == " ":
            b += ""
    return b
  
