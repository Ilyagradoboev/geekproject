def exponent(a, b):
    """Функция, использующая ** """
    b = abs(b)
    return a ** b


print(exponent(3, -10))


def exp(a, b):
    """Функция, использующая * """
    result = a
    b = abs(b)
    for i in range(b - 1):
        b -= 1
        result = result * a
    return result


print(exp(3, -10))


def xp(a, b):
    """Рекурсивная функция, использующая + """
    b = abs(b)
    if b == 1:
        return a
    else:
        x = 0
        for i in range(a):
            x = xp(a, b - 1) + x
        return x


print(xp(3, -10))
