
my_list = []
class MyExc(Exception):
    def __init__(self, num):
        if num.isdigit():
            my_list.append(num)
        else:
            print('Вы ввели не число')





while True:
    x = input('Введите число, или stop для завершения ')
    if x == 'stop':
        print(my_list)
        break
    else:
        MyExc(x)

