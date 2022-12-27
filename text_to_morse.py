#Переводит строку в азбуку Морзе
morse = {'А': '·−', 'Б': '−···', 'В': '·−−', 'Г': '−−·', 'Д': '−··', 'Е': '·', 'Ж': '···−', 'З': '−−··', 'И': '··', 'Й': '·−−−', 'К': '−·−', 'Л': '·−··', 'М': '−−', 'Н': '−·', 'О': '−−−', 'П': '·−−·', 'Р': '·−·', 'С': '···', 'Т': '−', 'У': '··−', 'Ф': '··−·', 'Х': '····', 'Ц': '−·−·', 'Ч': '−−−·', 'Ш': '−−−−', 'Щ': '−−·−', 'Ъ': '·−−·−·', 'Ы': '−·−−', 'Ь': '−··−', 'Э': '··−··', 'Ю': '··−−', 'Я': '·−·−'}
text = 'Я умею программировать'
string = ''  #создаем строку для перевода
for letter in text:  #для каждой буквы в тексте 
	letter = letter.upper()  #повысить ее до заглавной
	if letter in morse:   #если такая буква есть в словаре morse
		string += morse[letter]  #добавить значение из словаря morse в string
	elif letter == ' ':   #если в тексте пробел
		string += ' '     #добавляем просто пробел
	else:
		print('Error')
		break
print(string)









