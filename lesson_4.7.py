import functools

def fact(n):
    yield functools.reduce(lambda x,y: x * y, [el for el in range(1, n+1)])

for el in fact(6):
    print(el)

g = fact(5)
print(g)

def factor(n):
    factorial = 1
    for el in range(1, n+1):
        factorial = factorial * el
        yield factorial


for el in factor(6):
    print(el)