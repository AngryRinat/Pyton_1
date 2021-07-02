

def thesaurus_adv(*list):
    new_dict = {}

    for lis in list:
        name_and_surname = lis.split(' ')   #Разделяем строку по пробелу на 2 элемента
        name = name_and_surname[0][0]       # Первая буква имени
        surname = name_and_surname[1][0]    # Первая буква фамилии


        if surname not in new_dict:          # Если первой буквы фамилии нет в ключах словаря, то
            new_dict[surname] = {name: []}   # добавляем - первая буква фамилии - ключ, значение - словарь (первая буква имени, пустой список)


        if name not in new_dict[surname]:    # Если первой буквы имени нет в ключе с первой буквой фамилии, добавляем.
            new_dict[surname][name] = []


        new_dict[surname][name].append(lis)


    print(dict(sorted(new_dict.items())))


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Савва Ананьева", "Иван Бабушкин")

