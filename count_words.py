some_oxy_text = '''
Весь мой рэп, если коротко, про то, что
Уж который год который город под подошвой
В гору, когда прет. Потом под гору, когда тошно
Я не то, что Гулливер, но все же город под подошвой
Город под подошвой, город под подошвой
Светофоры, госпошлины, сборы и таможни
Я не знаю, вброд или на дно эта дорожка
Ты живешь под каблуком, у меня - город под подошвой
'''

import re
res = {}
splitted_text = re.sub(r'[^\w\s]', '', some_oxy_text).lower().split()

for word in splitted_text:
    res.setdefault(word, 0)
    res[word] += 1
for word, count in res.items():
    print(f'{word}: {count}')