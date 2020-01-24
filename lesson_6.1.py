import time, itertools

class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        print(self.__color)
        time.sleep(7)
        self.__color = "Желтый"
        print(self.__color)
        time.sleep(2)
        self.__color = "Зеленый"
        print(self.__color)

Tlight = TrafficLight('Красный')
Tlight.running()

print('\nВторой вариант:')

class TrafficLight2:
    def __init__(self):
        self.__color = ""
        colors = ["Красный", "Желтый", "Зеленый"]
        self.__iterator = itertools.cycle(colors)

    def switch(self):
        self.__color = next(self.__iterator)

    def running(self):
        self.switch()
        print(self.__color)
        time.sleep(7)
        self.switch()
        print(self.__color)
        time.sleep(2)
        self.switch()
        print(self.__color)

Tlight2 = TrafficLight2()
Tlight2.running()