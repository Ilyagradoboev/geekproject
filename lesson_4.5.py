import functools

list = functools.reduce(lambda x,y: x * y, [el for el in range(100, 1001) if el % 2 == 0])

print(list)