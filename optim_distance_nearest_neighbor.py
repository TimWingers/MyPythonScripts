# Оптимизационный алгоритм Пути коммивояжера
# Алгоритм ближайшего соседа.
# вместо того чтобы перебирать все возможные маршруты (как бы это делалось
# методом грубой силы) здесь на каждом шаге мы находим только ближайшего соседа
import numpy as np
import math

# сгенерируем случайную карту, по которой будет перемещаться коммивояжер
random_seed = 1729  #фиксации изначального сета рэндома
np.random.seed(random_seed)
N = 40  # число пар координат для каждого города
x = np.random.rand(N)
y = np.random.rand(N)
points = zip(x,y) #соединяем значения x y для создание списка координат для каждого города
cities = list(points)
itinerary = list(range(0,N))

# Теперь зададим функцию для вычисления расстояния.
def howfar(lines):
  distance = 0 # Сначала общее расстояние определяется равным 0,
  for j in range(0,len(lines)):
    distance += math.sqrt(abs(lines[j][1][0] - lines[j][0][0])**2 + \
    abs(lines[j][1][1] - lines[j][0][1])**2)
# после чего для каждого элемента в списке lines к переменной distance
# прибавляется длина этого отрезка. Для вычисления длин отрезков
# используется теорема Пифагора.
  return(distance)

# Пришло время написать функцию поиска ближайшего соседа
def findnearest(cities,idx,nnitinerary):
  point = cities[idx] #Предположим, имеется точка point и индекс cities
  mindistance = float('inf')
  minidx = - 1
  for j in range(0,len(cities)):
    distance = math.sqrt((point[0] - cities[j][0])**2 + (point[1] - cities[j][1])**2)
    # вычисляем расстояние согласно теоремы Пифагора
    if distance < mindistance and distance > 0 and j not in nnitinerary:
      mindistance = distance
      minidx = j
  return(minidx)

# Наша цель — построить маршрут, который будет называться nnitinerary.
def donn(cities,N): # сокращение от DO Nearest Neighbour
  nnitinerary = [0] #выберем первый город, с которого начнется перемещение коммивояжера
  for j in range(0, N - 1):
#Если маршрут должен состоять из N городов, мы должны перебрать все числа от 0 до N–1 
    next = findnearest(cities,nnitinerary[len(nnitinerary) - 1],nnitinerary)
#для каждого из этих чисел найти соседа, ближайшего к последнему посещенному городу 
    nnitinerary.append(next)
#и присоединить этот город к маршруту 
  return(nnitinerary)
# Функция начинает с первого города из cities и на каждом шаге добавляет в
# маршрут город, ближайший к последнему посещенному, пока все города не будут
# включены в маршрут
# Чтобы получить представление о том, что означает этот результат, полезно 
# построить диаграмму маршрута. Для этого мы создадим функцию plotitinerary()
import matplotlib.collections as mc
import matplotlib.pylab as pl
def plotitinerary(cities,itin,plottitle,thename):
  lc = mc.LineCollection(genlines(cities,itin), linewidths=2)
  fig, ax = pl.subplots()
  ax.add_collection(lc)
  ax.autoscale()
  ax.margins(0.1)
  pl.scatter(x, y)
  pl.title(plottitle)
  pl.xlabel('X Coordinate')
  pl.ylabel('Y Coordinate')

plotitinerary(cities,donn(cities,N),'TSP - Nearest Neighbor','figure3')

# Можно также проверить, какое расстояние коммивояжеру придется преодолеть
# по новому маршруту:
print(howfar(genlines(cities,donn(cities,N))))
# Экономия более чем на 60% по сравнению со случайным объездом городов!