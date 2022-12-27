import random, time
print("Кто кого на игральных костях?")
Attempt = 0
YourNumber = 0
MyNumber = 0

#Создаем цикл бросков кубиков
while Attempt < 5 :  #Пока число попыток меньше 5
  Attempt = Attempt + 1  #Добавляем к счетчику попыток 1
  print(str(Attempt) + ". Раунд")
  print("Твой бросок: ", end="")
  Shoot1 = random.randint(1,6) #Случайное число броска 2 игрока
  time.sleep(1) # Ожидание в секунду
  print(Shoot1)
  print("Мой бросок: ", end="")
  Shoot2 = random.randint(1,6) #Случайное число броска 1 игрока
  time.sleep(1) # Ожидание в секунду
  print(Shoot2)
  if Shoot1 > Shoot2 :  #Если 2 игрок выбросил больше 1
    YourNumber = YourNumber + 1  #Увеличиваем его счетчик на 1
  if Shoot1 < Shoot2 :  #Если 1 игрок выбросил больше 2
    MyNumber = MyNumber + 1    #Увеличиваем его счетчик на 1
  print(str(YourNumber) + " и " + str(MyNumber))  #Выводим счет партии
  time.sleep(1.5) #Делаем паузу. Ожидание в 1,5 секунды
  print()

# Вычисления
if YourNumber > MyNumber :
  print("Ты выиграл")
elif YourNumber < MyNumber :
  print("Я выиграл")
else :
  print("Ничья")