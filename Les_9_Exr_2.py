
class Road:

    def __init__(self, _lenght, _weight):
        self._lenght = _lenght
        self._weight = _weight
        self.coff_1 = 1
        self.coff_2 = 1

    def covering(self):
        mass = self._lenght * self._weight * self.coff_2 * self.coff_1
        print(mass)



road1 = Road(5, 4)

road1.covering()
