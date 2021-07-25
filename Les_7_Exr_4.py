import os

folder = 'E:\Катя Вентз\Брошюра VDD'
os.chdir('E:\Катя Вентз\Брошюра VDD')

new_dict = {}
new_list = []

for item in os.listdir(folder):
    new_list.append(os.path.getsize(item))

ran = len(str(max(new_list)))

for i in range(ran+2):
    if i == 0:
        new_dict[i] = 0
    else:
        new_dict[10**i] = 0


for i in range(len(new_list)):
    for key in new_dict:

        if key/10 < new_list[i] < key:

            new_dict[key] += 1



print(new_dict)


#.st_size объекта os.stat.