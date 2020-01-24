class Car:
    def __init__(self, color, name, maxSpeed, is_police=False):
        self.maxSpeed = maxSpeed
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed == 0:
            print(f'Машина {self.name} поехала')
        else:
            print(f'Машина {self.name} уже в движении')

    def accelerate(self):
        if self.speed < self.maxSpeed:
            self.speed += 20
            print(f'Скорость машины {self.name} увеличилась')
        else:
            print(f'Для машины {self.name} уже достигнута максимальная скорость')

    def brake(self):
        if self.speed > 20:
            self.speed -= 20
            print(f'Скорость машины {self.name} уменьшилась')
        else:
            self.speed -= 20
            print(f'Машина {self.name} остановилась')

    def stop(self):
        if self.speed == 0:
            print(f'Машина {self.name} уже остановлена')
        else:
            print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        if direction == 'right':
            print(f'Машина {self.name} повернула направо')
        elif direction == 'left':
            print(f'Машина {self.name} повернула налево')
        else:
            print('Для поворота используйте параметры left и right')

    def show_speed(self):
        print(f'Машина {self.name} движется со скоростью {self.speed}')


class TownCar(Car):
    def __init__(self, color, name, maxSpeed):
        super().__init__(color, name, maxSpeed)

    def show_speed(self):
        print(f'Машина {self.name} движется со скоростью {self.speed}')
        if self.speed > 60:
            print('Превышение скорости! Снизьте скорость!')


class SportCar(Car):
    def __init__(self, color, name, maxSpeed):
        super().__init__(color, name, maxSpeed)


class WorkCar(Car):
    def __init__(self, color, name, maxSpeed):
        super().__init__(color, name, maxSpeed)

    def show_speed(self):
        print(f'Машина {self.name} движется со скоростью {self.speed}')
        if self.speed > 40:
            print('Превышение скорости! Снизьте скорость!')


class PoliceCar(Car):
    def __init__(self, color, name, maxSpeed, is_police=True):
        super().__init__(color, name, maxSpeed)
        self.is_police = is_police


car1 = TownCar('Red', 'Viper', 100)
car1.go()
car1.accelerate()
car1.turn('left')
car1.accelerate()
car1.accelerate()
car1.accelerate()
car1.show_speed()
car1.brake()
car1.show_speed()
car1.brake()
car1.brake()
car1.show_speed()
car1.stop()

car2 = PoliceCar('Blue', 'Toyota', 120)
car2.go()
car2.accelerate()
car2.turn('left')
car2.accelerate()
car2.accelerate()
car2.accelerate()
car2.accelerate()
car2.accelerate()
car2.accelerate()
car2.show_speed()
car2.brake()
car2.show_speed()
car2.brake()
car2.brake()
car2.show_speed()
car2.stop()