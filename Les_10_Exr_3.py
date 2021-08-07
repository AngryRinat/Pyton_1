class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        sum = self.count + other.count
        new_cell = Cell(sum)
        return new_cell

    def __str__(self):
        return str(self.count)

    def __sub__(self, other):
        if self.count - other.count > 0:
            new_cell = self.count - other.count
            return new_cell

        else:
            print('There is no possibilities to substract')

    def __mul__(self, other):
        new_cell = self.count * other.count
        return new_cell

    def __truediv__(self, other):
        if self.count > other.count:
            eq = self.count // other.count
        else:
            eq = other.count // self.count

        return eq

    def make_order(self, number):
        d = self.count // number
        d_o = self.count % number
        str = (('*' * number) + '\n') * d + '*' * d_o

        return str


onecell = Cell(158)

twocell = Cell(100000000000)

threecell = onecell / twocell

print(onecell.make_order(150))
