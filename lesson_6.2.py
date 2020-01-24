class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def concrete(self):
        return self._length * self._width * 25 * 5

newRoad = Road(10000, 12)
print(newRoad.concrete())