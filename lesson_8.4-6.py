class Storage:
    def __init__(self, name):
        self.name = name
        self.positions = {}

    def income(self, *positions):
        newpositions = list(positions)
        for position in newpositions:
            if self.positions.get(position.name) == None:
                self.positions.update({position.name: position.quantity})
            else:
                new_quantity = position.quantity + self.positions.get(position.name)
                self.positions.update({position.name: new_quantity})

    def outcome(self, direction, *positions):
        positions = list(positions)
        for position in positions:
            try:
                if self.positions.get(position.name) == None:
                    raise Exception
            except Exception:
                print('Данной позиции нет на складе, операция невозможна!')
            else:
                new_quantity = self.positions.get(position.name) - position.quantity
                direction.income(position)
                if self.positions.get(position.name) > 1:
                    self.positions.update({position.name: new_quantity})
                else:
                    self.positions.pop(position.name)


class OfficeEquip:
    def __init__(self, name, quantity, format, connection):
        self.name = name
        try:
            self.quantity = int(quantity)
        except ValueError:
            print("Значение поля количество должно состоять из цифр!")
        self.format = format
        self.connection = connection


class Printer(OfficeEquip):
    def print(self):
        print(self.name + " печатает")


class Scaner(OfficeEquip):
    def scan(self):
        print(self.name + " сканирует")


class Copier(OfficeEquip):
    def copy(self):
        print(self.name + " копирует")


class MFU(Printer, Scaner, Copier):
    def mailscan(self):
        print(self.name + " сканирует и отправляет по e-mail")


mfu = MFU("МФУ", "r", "A3", "LAN")
printer = Printer("Принтер", "1", "A4", "USB")
storage = Storage('Склад')
it = Storage('IT')

storage.income(mfu, mfu, mfu)
storage.income(mfu, printer)
storage.outcome(it, mfu)
storage.outcome(it, mfu)
storage.outcome(it, mfu)
storage.outcome(it, mfu)

print(storage.positions)
print(it.positions)

mfu.copy()
mfu.print()
mfu.scan()
mfu.mailscan()
printer.print()
