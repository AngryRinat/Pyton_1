tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В'
]

def class_gen(list1, list2):
    dict1 = {}
    for i in range(len(list1)):
        if i >= len(list2):
            list2.append(None)
        dict1[list1[i]] = list2[i]
        yield dict1

n = class_gen(tutors, klasses)


print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))

