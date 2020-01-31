class DivideError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


a = 10
b = 0
try:
    if b == 0:
        raise DivideError('Деление на ноль недопустимо!')
    c = a / b
except DivideError as e:
    print(e)
else:
    print(c)
