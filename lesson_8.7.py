class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return f'{self.x}, {self.y}'

    def __sub__(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        return f'{self.x}, {self.y}'

    def __mul__(self, other):
        self.x = self.x * other.x - self.y * other.y
        self.y = self.x * other.y + other.x * self.y
        return f'{self.x}, {self.y}'

    def __str__(self):
        return f'{self.x}, {self.y}'


a = Complex(1, 5)
b = Complex(2, 0)

# print(a - b)
print(a + b)
print(a * b)
