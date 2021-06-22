qube_list = []
new_list = []
for i in range(1, 1001, 2):
    n = i**3
    qube_list.append(n)

for i in range(len(qube_list)):
    count = 0
    n_number = qube_list[i]


    while (n_number*10) // 10 != 0:

            number = n_number % 10

            n_number //= 10

            count += number


    if count % 7 == 0:
        #print(count, qube_list[i])
        new_list.append(round(qube_list[i]**(1/3)))

print(new_list)

qube_list = []
new_list = []

for i in range(1, 1001, 2):
    n = i**3 + 17
    qube_list.append(n)

for i in range(len(qube_list)):
    count = 0
    n_number = qube_list[i]


    while (n_number*10) // 10 != 0:

            number = n_number % 10

            n_number //= 10

            count += number


    if count % 7 == 0:
        #print(count, qube_list[i])
        new_list.append(round(qube_list[i]**(1/3)))

print(new_list)


