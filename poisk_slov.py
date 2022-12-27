#Поиск слов в предложении
import re
text = "The one perfectly divine thing, the one glimpse of God’s paradise given on earth, is to fight a losing battle - and not lose it."
word_list = ['The','one','perfectly','divine']
# определяем переменную locs (сокр. от locations); она содержит позиции
# каждого слова из списка в тексте
locs = list(set([(m.start(),m.end()) 
            for word in word_list 
            for m in re.finditer(word, text)]))
# Списковое включение размещается в квадратных скобках ([]).
# Конструкция for word in word_list перебирает все слова из списка word_list.
# Для каждого слова вызывается функция re.finditer(), которая находит выбранное
# слово в тексте и возвращает список всех позиций, в которых оно встречается.
# Эти позиции последовательно перебираются, и каждая отдельная позиция
# сохраняется в m. При обращении к m.start() и m.end() мы получаем 
# соответственно позицию начала и конца слова в тексте. 
# Все списковое включение заключается в list(set()).
# Это удобный способ получить список, который содержит только уникальные
# значения без дубликатов. 
print(locs)
# [(36, 39), (4, 7), (18, 24), (8, 17), (0, 3)]
text[36:39] #one
text[4:7] #one
text[18:24] #divine
text[8:17] #perfectly
text[0:3] #the