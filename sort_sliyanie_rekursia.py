#Сортировка слиянием через рекурсию
import math  #импорт библиотеки math

def merging(left,right):  #создаем функцию слияния 2 списков
  newcabinet = []         #создаем пустой список для сорт.значений
  while(min(len(left),len(right)) > 0):  #пока длина списков больше 0
    if left[0] > right[0]:  #если значение в левом списке > правого
      to_insert = right.pop(0)  #забираем значение из правого
      newcabinet.append(to_insert)  #и кладем его в новый список
    elif left[0] <= right[0]:  #если значение в левом <= правого
      to_insert = left.pop(0)  #забираем его из левого 
      newcabinet.append(to_insert)  #и кладем в новый список
  if(len(left) > 0):  #если длина левого больше 0
    for i in left:    #то пробегаемся по нему
      newcabinet.append(i)  #и добавляем его значения в новый
  if(len(right) > 0):  #если длина правого больше 0
    for i in right:   #то пробегаемся по нему
      newcabinet.append(i)  #и добавляем значения в новый
  return(newcabinet)  #выводим новый список

def mergesort(cabinet): #создаем функцию рекурсии
  newcabinet = []       #создаем пустой список для сорт.значений
  if(len(cabinet) == 1): #если наш список содержит 1 значение
    newcabinet = cabinet #то он просто ему равен (ограничение рекурсии)
  else:  #иначе
    #разделяем список на левую и правую части
    left = mergesort(cabinet[:math.floor(len(cabinet)/2)])
    right = mergesort(cabinet[math.floor(len(cabinet)/2):])
    #и передаем их функцию merging
    newcabinet = merging(left,right)
  return(newcabinet)  #выводим новый список

cabinet = [47,78,97,68,51,55,21,10,64,42,18,36,13,81,38,56,64,30,67]
mergesort(cabinet)