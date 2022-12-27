# Бинарный поиск
# Базируется на том, что лучшая стратегия поиска основана 
# на предположении что не найдя искомое значение
#надо сужать границы поиска и делить их ровно на половину.

import math #для исп-я функции floor(), преобразующей дробные числа в целые

sorted_cabinet = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]

def binarysearch(sorted_cabinet,looking_for):
  guess = math.floor(len(sorted_cabinet)/2) #предположим, что значение находится в середине
  upperbound = len(sorted_cabinet)  #Изнач. верхняя граница позиции
  lowerbound = 0                    #Изнач. нижняя граница позиции
  while(abs(sorted_cabinet[guess] - looking_for) > 0.0001):
  #ограничение рекурсии - пока положит. разность (abs) больше 0.0001 
    if(sorted_cabinet[guess] > looking_for):
    #если предполагаемое значение больше искомого  
      upperbound = guess  #сдвигаем верхнюю границу на предполагаемое
      guess = math.floor((guess + lowerbound)/2) #и делим оставшийся список на 2
    if(sorted_cabinet[guess] < looking_for):
    #если предположенное значение больше искомого  
      lowerbound = guess  #сдвигаем нижнюю границу на предполагаемое
      guess = math.floor((guess + upperbound)/2) #и делим оставшийся список на 2
  return(guess)

print(binarysearch(sorted_cabinet,16))
# 7. То есть число 16 занимает 7 позицию в списке