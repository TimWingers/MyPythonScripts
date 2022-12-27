houses_traits = {
'Slytherin': ['хитрость', 'находчивость', 'амбициозность'],
'Gryffindor': ['храбрость', 'благородство', 'честность'],
'Hufflepuff': ['честность', 'верность', 'трудолюбие'],
'Ravenclaw': ['мудрость', 'ум', 'творчество']
}

new_magicians = {
'Arabella Skeeter': ['хитрость', 'творчество', 'находчивость'],
'Stan Malfoy': ['амбициозность', 'благородство', 'храбрость'],
'Morgana Granger': ['трудолюбие', 'верность', 'мудрость']
}

for name, personal_traits in new_magicians.items():
#Перебираем каждое имя и параметры в 2 словаре
	matches = {'Slytherin': 0, 'Gryffindor':0, 'Hufflepuff':0, 'Ravenclaw':0}
#Создаем новый словарь matches (совпадения)
	for house, house_traits in houses_traits.items():
#Перебираем каждое имя и параметры в 1 словаре
		matches[house] += len(set(house_traits).intersection(personal_traits))
#Добавляем в словарь matches в качестве ключей house,
# а в качестве значений длину множеств совпадений параметров
	print(f'{name}: {matches}')
    
#Arabella Skeeter: {'Slytherin': 2, 'Gryffindor': 0, 'Hufflepuff': 0, 'Ravenclaw': 1}
#Stan Malfoy: {'Slytherin': 1, 'Gryffindor': 2, 'Hufflepuff': 0, 'Ravenclaw': 0}
#Morgana Granger: {'Slytherin': 0, 'Gryffindor': 0, 'Hufflepuff': 2, 'Ravenclaw': 1}