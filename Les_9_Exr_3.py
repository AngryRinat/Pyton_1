class Worker:

    def __init__(self, name, surname, position, _income):

        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

class Position(Worker):

    def get_full_name(self):
        print(f'The Worker name is {self.name}, surname is {self.surname}, position is {self.position}')

  #  def get_total_income(self):



mister = Worker('Bill', 'Edwards', 'Miller', 4000)



print(mister._income)