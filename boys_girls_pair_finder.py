#Пример сравнения длины списков и их матчинга между собой
def pair_finder(boys, girls):
    if len(boys) == len(girls):
        boys.sort()
        girls.sort()
        print('Идеальные пары: ')
        for name in range(len(boys)):
            print(boys[name], 'и', girls[name])
    else:
        print('Внимание, кто-то может остаться без пары!')
        
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
pair_finder(boys, girls)