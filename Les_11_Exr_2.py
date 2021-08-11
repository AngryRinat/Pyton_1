class MyZeroDivision(Exception):
    def __init__(self, num):
        if num == 0:
            print('Нельзя вводить ноль')





x = int(input('Введите делитель: '))

MyZeroDivision(x)
