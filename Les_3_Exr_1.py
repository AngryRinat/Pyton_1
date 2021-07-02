translator_dict = { 'один': 'one', 'два': 'two', 'три': 'three', 'четыре': 'four', 'пять': 'five',
                    'шесть': 'six', 'семь': 'seven', 'восемь': 'eight', 'девять': 'nine'}

def translator(word):
    answer = translator_dict.get(word.lower())
    if word[0].isupper():
       answer = answer.capitalize()
    return answer

print(translator('Один'))
