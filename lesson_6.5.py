class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Выполняется отрисовка')

class Pen(Stationery):
    def draw(self):
        print('Пишем текст')

class Pencil(Stationery):
    def draw(self):
        print('Делаем пометки')

class Handle(Stationery):
    def draw(self):
        print('Выделяем текст')

Pen = Pen("Ручка")
Pencil = Pencil("Карандаш")
Handle = Handle("Маркер")

Pen.draw()
Pencil.draw()
Handle.draw()