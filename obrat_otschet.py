# Version 1
import time
for i in range (10, 0, -1):
  print (i)
  time.sleep(1)
print('Start!')


# Version 2
import time
seconds = int(input("Таймер обратного отсчета: Сколько секунд? "))
for i in range (seconds, 0, -1):
  for star in range(0, i):
      print ('*', end=" ")  #рисует строку
  print (i)
  time.sleep(1)
print ("ПУСК!")