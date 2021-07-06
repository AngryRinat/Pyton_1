tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В'
]

def class_gen(list1, list2):
    for i in range(len(list1)):
        if i >= len(list2):
            list2.append(None)
        tup_tmp = (list1[i], list2[i])
        yield tup_tmp

n = class_gen(tutors, klasses)
print(type(class_gen(tutors, klasses)))
print(type(next(n)))


print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
