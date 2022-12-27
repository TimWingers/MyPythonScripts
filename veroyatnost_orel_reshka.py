#Вероятность выпадения на монете 10 орлов подряд
from random import *
coin = ["Heads", "Tails"]   #Создаем список с орлами и решками
heads_in_row = 0            #Здесь считаем орлов подряд
ten_heads_in_row = 0        #Здесь считаем случаи 10 орлов подряд 
attempts = 100000           #Число попыток

for i in range (attempts):
  if choice(coin) == "Heads":  #Если выпадает орел
    heads_in_row += 1          #Прибавляем к списку орлов подряд 1
  else:                        #Иначе
    heads_in_row = 0           #Обнуляем счетчик
  if heads_in_row == 10:       #Если мы достигли 10 орлов подряд
    ten_heads_in_row += 1      #Записываем событие в переменную
    heads_in_row = 0           #Обнуляем счетчик

probability = round(attempts / ten_heads_in_row)
print (f"В результате {attempts} попыток мы получили 10 орлов подряд {ten_heads_in_row} раз.")
print (f'То есть вероятность этого события 1 раз на ~ {probability} бросков.')