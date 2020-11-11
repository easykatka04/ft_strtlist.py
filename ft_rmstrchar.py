def ft_rmstrchar(a, b):
    c = ""
    for i in a:
        if i not in b:
            c += i
        if i in b:
            c += ""
    return c
  
