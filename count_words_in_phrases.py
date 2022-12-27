from collections import Counter
def phrase_counter(queries):
    wordcount = []
    for phrase in queries:
        words = phrase.split(' ')
        wordcount.append(len(words))

    combine = dict(Counter(wordcount))
    for key, value in combine.items():
        print (f'Поисковых запросов, содержащих {key} слов(а): {value} ({(value/(len(wordcount)))*100 :.2f}%)')
    

queries = ['смотреть сериалы онлайн','новости спорта','афиша кино','курс доллара',
           'сериалы этим летом','курс по питону','сериалы про спорт',]
phrase_counter(queries)