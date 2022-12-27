import random
import time
suits = ['пики', 'бубны', 'черви', 'крести']
faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
my_score = 0
comp_score = 0
keep_going = True

while keep_going:
  my_face = random.choice(faces)
  comp_face = random.choice(faces)
  my_suit = random.choice(suits)
  comp_suit = random.choice(suits)
  print('Перетасовываем колоду')
  time.sleep(2)
  print(f'Беру карту')
  time.sleep(1)
  print(f'У меня {my_face} {my_suit}.')
  time.sleep(1)
  print('Теперь очередь взять карту у компьютера')
  time.sleep(1.5)
  print (f'У компьютера {comp_face} {comp_suit}')
  time.sleep(0.5)
  if faces.index(my_face) > faces.index(comp_face):
    my_score += 1
    print(f'Я победил! Счет {my_score} - {comp_score}')
  elif faces.index(my_face) < faces.index(comp_face):
    comp_score += 1
    print(f'Победил компьютер. Счет {my_score} - {comp_score}')
  else:
    print(f'У нас ничья! Счет {my_score} - {comp_score}')
  answer = input('Нажмите [Enter] чтобы продолжить или любую клавишу чтобы выйти ')
  keep_going = (answer == "")