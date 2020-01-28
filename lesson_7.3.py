class Cell:
    def __init__(self):
        self.slot = 8

    def __call__(self, *args, **kwargs):
        return self.slot

    def __add__(self, other):
        self.slot = self.slot + other.slot
        return self.slot


    def __sub__(self, other):
        if self.slot != other.slot:
            self.slot = abs(self.slot - other.slot)
            return self.slot
        else:
            print("Ошибка, количество ячеек одинаково!")


    def __mul__(self, other):
        self.slot = self.slot * other.slot
        return self.slot

    def __truediv__(self, other):
        if self > other:
            self.slot = round(self.slot / other.slot)
        else:
            self.slot = round(other.slot / self.slot)
        return self.slot

    def __lt__(self, other):
        return self.slot > other.slot

    def make_order(self, iter):
        a = self.slot // iter
        b = self.slot % iter
        string = ''
        for i in range(a):
            string = string + '*' * iter + '\n'
        string = string + '*' * b
        return string

new_cell = Cell()
new_cell2 = Cell()
new_cell3 = Cell()
new_cell3(new_cell() + new_cell2())
print(new_cell.__add__(new_cell2))

print(new_cell.__mul__(new_cell2))
print(new_cell.__sub__(new_cell2))
print(new_cell2.__truediv__(new_cell3))
print(new_cell())

print(Cell.make_order(new_cell, 16))