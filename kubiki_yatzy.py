#Яцзы - игра на выпадение 3, 4 или 5 одинаковых кубиков из 5
import random
#Игровой цикл
keep_going = True
while keep_going:
  #Выброс 5 случайных кубиков
  dice = [0,0,0,0,0] #создаем список для 5 значений dice[0]-dice[4]
  for i in range(5): #для каждого из кубиков в диапазоне 1-5
    dice[i] = random.randint(1,6) #присвоить случайное число в диапазоне 1-6
  print('Вам выпало:', dice)  #показать выпавшие значения
  #Отсортировать их
  dice.sort()
  #Проверка комбинации 5ти, 4х, или 3х одинаковых кубиков
  #Выпало Яцзы - все 5 кубиков одинаковые
  if dice[0] == dice[4]:  #если 1й элемент списка = последнему
    print('Яцзы!')
  #Выпало 4 одинаковых кубика (первые четыре или последние четыре)
  elif (dice[0] == dice[3]) or (dice[1] == dice[4]): 
    print('Четыре одинаковых!')
  #Выпало 3 одинаковых (первые три, три посередине или последние три)
  elif (dice[0] == dice[2]) or (dice[1] == dice[3]) or (dice[2] == dice[4]):
    print('Три одинаковых!')
  keep_going = (input('Нажмите [Enter] для продолжения или любую клавишу чтобы выйти ') == '')