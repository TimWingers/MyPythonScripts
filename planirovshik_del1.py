#Планировщик дел
print ("Привет! Я программа-планировщик дел. \n Со мной вы все успеете и ничего не забудете.")
print("Я помогу вам запланировать до 5 дел за раз. Вы говорите мне сначала дату, а потом задачу. \n Я все запомню! Попробуем?")

date1 = input("Введите дату: ")
actions1 = input("Введите задачу: ")
print("Вы запланировали:")
todo = {date1: actions1}
print(todo)
dialog1 = input("Будем планировать задачи еще? (да/нет)")	

if dialog1 == "да": 
  date2 = input("Введите дату: ")
  actions2 = input("Введите задачу: ")
  print("Вы запланировали:")
  toadd2 = {date2: actions2}
  todo.update(toadd2)
  print(todo)
  dialog2 = input("Будем планировать задачи еще? (да/нет)")
else:
  print ("Понял. Хорошего дня!")	
	
if dialog2 == "да":
  date3 = input("Введите дату: ")
  actions3 = input("Введите задачу: ")
  print("Вы запланировали:")
  toadd3 = {date3: actions3}
  todo.update(toadd3)
  print(todo)
  dialog3 = input("Будем планировать задачи еще? (да/нет)")
else:
  print ("Понял. Хорошего дня!")	

if dialog3 == "да":
  date4 = input("Введите дату: ")
  actions4 = input("Введите задачу: ")
  print("Вы запланировали:")
  toadd4 = {date4: actions4}
  todo.update(toadd4)
  print(todo)
  dialog4 = input("Будем планировать задачи еще? (да/нет)")
else:
  print ("Понял. Хорошего дня!")		

if dialog4 == "да":
  date5 = input("Введите дату: ")
  actions5 = input("Введите задачу: ")
  print("Вы запланировали:")
  toadd5 = {date5: actions5}
  todo.update(toadd5)
  print(todo)
  print("Неплохой список дел! Так держать!")     
else:
  print ("Понял. Хорошего дня!")