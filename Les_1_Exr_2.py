
qube_list = []

for i in range(1, 1001, 2):
    n = i**3
    qube_list.append(n)



count = 0
for i in range(len(qube_list)):
    m = qube_list[i]
    sum = (m // 1000) + ((m % 1000) // 100) + (((m % 1000) % 100) // 10) + (m % 10)
    if (sum % 7) == 0:
        count += sum

print(f'Сумма чисел равна {count}')


count = 0
for i in range(len(qube_list)):
    qube_list[i] = qube_list[i] + 17


for i in range(len(qube_list)):
    m = qube_list[i]
    sum = (m // 1000) + ((m % 1000) // 100) + (((m % 1000) % 100) // 10) + (m % 10)
    if (sum % 7) == 0:
        count += sum
print(f'Сумма чисел после прибавления 17 равна {count}')


