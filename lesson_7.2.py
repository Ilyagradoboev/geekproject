from abc import abstractmethod

class Clothes:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cons(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def cons(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def cons(self):
        return self.height * 2 + 0.3

    @property
    def summary(self):
        return f'На {self.name} будет истрачено {self.cons} ед. ткани'


new_coat = Coat("Пальто", 54)
new_suit = Suit("Костюм", 180)

Consumption = new_coat.cons() + new_suit.cons
print(Consumption)
print(new_suit.summary)
