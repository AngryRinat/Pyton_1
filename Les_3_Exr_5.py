import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n=3, replay=True):
    #Function get_jokes uses n(int), and replay(bool).
    #replay = False, when we use word from list only once.

    list2 = []
    for i in range(n):
         list1 = []
         n1 = random.choice(nouns)
         n2 = random.choice(adverbs)
         n3 = random.choice(adjectives)
         list1.append(n1)
         list1.append(n2)
         list1.append(n3)
         list2.append(' '.join(list1))
         if replay == False:
             nouns.remove(n1)
             adverbs.remove(n2)
             adjectives.remove(n3)
    print(list2)

get_jokes(1, True)