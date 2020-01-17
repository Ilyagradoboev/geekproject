def my_func(a, b, c):
    list = [a, b, c]
    list.sort(reverse=1)
    list.pop(-1)
    return list[0] + list[1]


print(my_func(8, 9, 4))
