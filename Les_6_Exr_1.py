from time import perf_counter
start = perf_counter()


file_1 = open('test.txt', 'r')
content = []
for line in file_1:
    list_con = line.split(' ')

    con_tuple = (list_con[0], list_con[5][1:], list_con[6])
    content.append(con_tuple)



list_ip = [el[0] for el in content]

list_count = set()
for el in list_ip:
    list_count.add(el)
list_count_list = list(list_count)

list_count_ip = []
for i in range(len(list_count_list)):
    list_count_ip.append([list_count_list[i], list_ip.count(list_count_list[i])])


new_list_count_ip = sorted(list_count_ip, key=lambda x: x[1], reverse=True)

print(f'Spammer is on adress: {new_list_count_ip[0][0]} with count of visits {new_list_count_ip[0][1]}')
print(perf_counter() - start)
