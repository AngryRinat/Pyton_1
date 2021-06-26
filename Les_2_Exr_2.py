my_list = ['в', '5', 'часов', '7', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
count = 1
sum_count =0
while count != 0:


    for i in range(len(my_list)):
        count = 0
        if my_list[i].isdigit():
            count += 1
            sum_count += 1
            if len(my_list[i]) < 2:
                    print(my_list[i])
                    my_list[i] = '0' + my_list[i][0]
                    print(my_list[i])

        elif my_list[i].startswith('+') or my_list[i].startswith('-'):
            sum_count += 1
            if len(my_list[i][1:]) < 2:
                my_list[i] = my_list[i][0] + '0' + my_list[i][1]
                print(my_list[i])


count = 1
while count != 0:
    for i in range(len(my_list)+sum_count * 2):
        count = 0

        if (my_list[i].isdigit() or my_list[i][1:].isdigit()) and (my_list[i - 1] != '"'):
            my_list.insert(i, '"')
            my_list.insert(i + 2, '"')
            print(my_list[i], my_list[i + 1], my_list[i + 2])
            count += 1


print(my_list)
print(len(my_list))

my_list[3] = ''.join(my_list[1:4]) + ' '.join(my_list[5:8])


print(my_list)












'''

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
count = 1

while count != 0:

    count = 0
    for i in range(len(my_list)):

        if (my_list[i].isdigit() or my_list[i][1:].isdigit()) and (my_list[i-1] != '"'):
            my_list.insert(i, '"')
            my_list.insert(i + 2,'"')
            #print(my_list[i], my_list[i+1], my_list[i+2])
            count += 1

            if my_list[i+1].startswith('+') or my_list[i+1].startswith('-'):
                if len(my_list[i+1][1:]) < 2:
                    my_list[i+1] = my_list[i+1][0] + '0' + my_list[i+1][1]
                    print(my_list[i])
"""
            else:
                if len(my_list[i+1]) < 2:
                    print(my_list[i+1])
                    my_list[i+1] ='0' + my_list[i+1][0]
                    print(my_list[i+1])

        #if (my_list[i].isdigit() or my_list[i][1:].isdigit()):

       #     my_list[i] = ''.join(my_list[i-1:i+2])
        #    print(my_list[i])

"""

my_str = ' "'.join(my_list)
print(my_str)

'''
