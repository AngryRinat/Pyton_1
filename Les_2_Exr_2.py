my_list = ['в', '15', 'часов', '7', 'минут', 'температура', 'воздуха', 'была', '+50', 'градусов']

count = 1   #Создаем счетчик, чтобы цикл while запустился

while count != 0:

    count = 0     #Обнуляем счетчик
    for i in range(len(my_list)):
         if (my_list[i].isdigit() or my_list[i][1:].isdigit()) and (my_list[i-1] != '"'):  #Добавляем в массив кавычки вокруг числе
            my_list.insert(i, '"')
            my_list.insert(i + 2,'"')
            count += 1

            if my_list[i+1].startswith('+') or my_list[i+1].startswith('-'):     #Определяем число с + и - в начале
                if len(my_list[i+1][1:]) < 2:
                    my_list[i+1] = my_list[i+1][0] + '0' + my_list[i+1][1]      #Добавляем нули в число, если требуется


            else:
                if len(my_list[i+1]) < 2:
                     my_list[i+1] ='0' + my_list[i+1][0]    #Добавляем нули в число, если требуется



print(my_list)

str1 = ' '.join(my_list[0:2])+my_list[2]+' '.join(my_list[3:6])+my_list[6]+ \
' '.join(my_list[7:13])+my_list[13] + ' '.join(my_list[14:16])   #Создаем требуемую строку
print(str1)






