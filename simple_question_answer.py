#Функция-тест, которая задает вопрос, получает ответ и
# сравнивает ответ с правильным значением. Чем больше
# правильных ответов, тем больше присваивается очков.

def check_guess(guess, answer):
  global score
  if guess.lower() == answer.lower():
    print('Это правильный ответ!')
    score = score + 1
  else:
    print('Нет, это неверный ответ.')

score = 0
maxscore = 3
print('Тест Автомобили')
guess1 = input('В какой стране производят BMW? ')
check_guess(guess1, 'Германия') 
guess2 = input('Что быстрее: Hyundai или Porsche? ')
check_guess(guess2, 'Porsche')
guess3 = input('Какой самый популярный электроавтомобиль? ')
check_guess(guess3, 'Tesla')
print(f'Вы набрали {score} очков из {maxscore} возможных')