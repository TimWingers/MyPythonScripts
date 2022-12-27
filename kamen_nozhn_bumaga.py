import random
choices = ['К', 'Н', 'Б']
player_score = 0
comp_score = 0
print('Правила: Камень давит ножницы. Ножницы режут бумагу. Бумага накрывает камень')
print()
player = input('Выберите: камень (К), ножницы (Н), бумага (Б) или выход (В)? ')
while player != 'В':
  player = player.upper()
  computer = random.choice(choices)
  print(f'Твой выбор {player}, компьютер выбрал {computer}')
  if player == computer:
    print(f'Ничья! Счет {player_score} - {comp_score}')
  elif player == 'К':
    if computer == 'Н':
      player_score += 1
      print(f'Ты победил! Счет {player_score} - {comp_score}')
    else:
      comp_score += 1
      print(f'Ты проиграл! Счет {player_score} - {comp_score}')
  elif player == 'Н':
    if computer == 'Б':
      player_score += 1
      print(f'Ты победил! Счет {player_score} - {comp_score}')
    else:
      comp_score += 1
      print(f'Ты проиграл! Счет {player_score} - {comp_score}')
  elif player == 'Б':
    if computer == 'К':
      player_score += 1
      print(f'Ты победил! Счет {player_score} - {comp_score}')
    else:
      comp_score += 1
      print(f'Ты проиграл! Счет {player_score} - {comp_score}')
  else:
    print('Кажется вы ошиблись в наборе')
  print()
  player = input('Выберите: камень (К), ножницы (Н), бумага (Б) или выход (В)? ')