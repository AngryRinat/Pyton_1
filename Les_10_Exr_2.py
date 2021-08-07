from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod  # Определяем абстрактные классы
    def change_size(self, *args):
        pass

    @abstractmethod
    def change_color(self, *args):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        self.color = 'black'
        self.tiss = round((size / 6.5 + 0.5), 2)
        self.__cost = 30000

    def __str__(self):
        return str(self.__cost)

    def change_size(self, size):
        self.size = size

    def change_color(self, color):
        self.color = color

    @property
    def change_cost(self):
        return self.__cost

    @change_cost.setter
    def change_cost(self, cost):

        if cost[0] < 0:
            print('Wrong information')
        else:
            self.__cost = cost


class Suite(Clothes):
    def __init__(self, tall):
        self.tall = tall
        self.tiss = round((2 * tall + 0.3), 2)

    def change_size(self, tall):
        self.tall = tall

    def change_color(self, color):
        self.color = color


jemper = Coat(35)
print(jemper)
jemper.change_size(34)
print(jemper.tiss)

new_su = Suite(2)
print(new_su.tiss)

jemper.change_cost = [50000]

print(jemper)
