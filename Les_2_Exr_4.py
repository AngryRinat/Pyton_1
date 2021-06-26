all_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']



for i in range(len(all_list)):
    all_list[i] = all_list[i].split()
    name = all_list[i].pop()
    print(f'Привет, {name.capitalize()}!')


