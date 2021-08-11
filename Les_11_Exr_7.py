class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def __mul__(self, other):
        res = (self.a * other.a - self.b * other.b)
        res_i = (self.a * other.b - other.a * self.b)
        return f'z = {res} + {res_i}i'

    def __add__(self, other):
        res = self.a + other.a
        res_i = self.b + other.b
        return f'z = {res} + {res_i}i'



num_1 = Complex(0,3)

num_2 = Complex(-5,4)

print(num_1 + num_2)








