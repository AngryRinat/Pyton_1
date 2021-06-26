#Функция, переводящая цену в формат "руб..коп"

def prices(elements):
    elements_rub = []
    for i in range(len(elements)):
        rub = int(elements[i] // 1)
        cop = int((elements[i] * 100) % 100)
        if cop == 0:
            cop = '00'
        elements_rub.append(f'{rub} руб {cop} коп')
    return elements_rub




#Создать список, содержащий цены на товары (10–20 товаров), например

my_list = [54.99, 40, 120, 34.50, 20.99, 30.69, 99.99]


#Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
my_list_new = []
print(prices(my_list))

#Вывести цены, отсортированные по возрастанию, новый список не создавать
print(prices(my_list), id(my_list))
my_list.sort()
print(prices(my_list), id(my_list))

#Создать новый список, содержащий те же цены, но отсортированные по убыванию.
my_list_revsort = my_list.copy()
my_list_revsort.sort(reverse = True)
print(prices(my_list_revsort))

#Вывести цены пяти самых дорогих товаров.
print(prices(my_list[:6]))



