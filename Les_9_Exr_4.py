
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('The car is riding')

    def stop(self):
        print('The car has just stopped')

    def turn(self, direction):
        print(f'The car has just turn to the {direction}')

    def show_speed(self):
        pass

class TownCar(Car):
    def show_speed(self):
        def show_speed(self):
            if self.speed <= 60:
                print(f'Cars velosity is {self.speed}')
            else:
                print('Your are exceeding the speed limit!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            print(f'Cars velosity is {self.speed}')
        else:
            print('Your are exceeding the speed limit!')

class PoliceCar(Car):
    pass

teana = WorkCar(150, 30, 'Nissan', False)
print(teana.is_police)
