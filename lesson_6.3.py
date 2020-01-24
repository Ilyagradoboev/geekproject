income = {
    'wage': 1000,
    'bonus': 250
}

class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' +self.surname

    def get_full_income(self):
        return self._income['wage'] + self._income['bonus']

seller = Position('Вася', 'Гуляев', 'Продавец')
manager = Position('Антон', 'Грушин', 'Менеджер')
print(seller.get_full_name())
print(seller.get_full_income())
print(manager.get_full_name())
print(manager.get_full_income())