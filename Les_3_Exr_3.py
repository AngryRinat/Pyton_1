
name_list = ("Иван", "Мария", "Петр", "Илья", "Ираклий", "Игорь", "Ирина", "Аарон")

def thesaurus (list):
    new_list = []
    new_dict = []
    for i in range(len(list)):
        p = list[i][0]
        if p not in new_list:
            new_list.append(p)
    for i in range(len(list)):
        n = new_list.index(list[i][0])
        new_dict.append(list[i])
    new_dict = {}
    for i in range(len(new_list)):
        new_dict.setdefault(new_list[i], [])
        for j in range(len(list)):
            if list[j].startswith(new_list[i]):
                new_dict[new_list[i]].append(list[j])
    return dict(sorted(new_dict.items()))

print(thesaurus(name_list))


