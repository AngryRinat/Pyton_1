
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 11, 11, 12, 12, 12]
#Первый способ решения, в лоб
'''
result = []
for i in range(len(src)):
    if src[i] in result:
        continue
    result.append(src[i])

#result.sort()
print(result)
'''
#Второй способ решени, используя множество
src_tmp = set()
src_new = []
for i in src:
   if i not in src_tmp:
      src_new.append(i)
      src_tmp.add(i)
print(src_new)