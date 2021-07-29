class TrafficLight:

    def __init__(self, _color):
        self._color = _color

    def running(self):

        if self._color == 'red':
            self._color = 'yellow'
        elif self._color == 'yellow':
            self._color = 'green'

        elif self._color == 'green':
            self._color = 'red'


my_light = TrafficLight('green')

my_light.running()

print(my_light._color)

my_light.running()
print(my_light._color)

my_light.running()
print(my_light._color)
