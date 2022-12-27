# Алгоритм Имитация отжига с поддержкой отмены
# (simulated annealing with cancelling)
# В процессе имитации отжига мы можем неосмотрительно принять однозначно
# плохое изменение маршрута. На такой случай будет полезно запомнить лучший
# маршрут, который был обнаружен на данный момент, и разрешить алгоритму
# вернуться к нему при определенных условиях
def perturb_sa3(cities,itinerary,time,maxitin):
# добавляем аргумент maxitin, который сообщает функции, сколько раз мы
# собираемся возвращаться, чтобы можно было точно определить текущую точку процесса
  neighborids1 = math.floor(np.random.rand() * (len(itinerary)))
  neighborids2 = math.floor(np.random.rand() * (len(itinerary)))
#определяем глобальные переменные mindistance для минимального расстояния,
# найденного на данный момент маршрута, при котором оно было достигнуто,
# и времени minitinerary, за которое оно было достигнуто.
# Если пройдет слишком много времени minidx и при этом не будет найдено
# ничего лучше маршрута с наименьшим расстоянием, то можно сделать вывод,
# что все изменения, внесенные после этой точки, были ошибочными и стоит
# вернуться к этому лучшему маршруту. 
  global mindistance
  global minitinerary
  global minidx
  itinerary2 = itinerary.copy()
  randomdraw = np.random.rand()
  randomdraw2 = np.random.rand()
  small = min(neighborids1,neighborids2)
  big = max(neighborids1,neighborids2)
  if(randomdraw2 >= 0.55):
    itinerary2[small:big] = itinerary2[small:big][::-1]
  elif(randomdraw2 < 0.45):
    tempitin = itinerary[small:big]
    del(itinerary2[small:big])
    neighborids3 = math.floor(np.random.rand() * (len(itinerary)))
    for j in range(0,len(tempitin)):
      itinerary2.insert(neighborids3 + j,tempitin[j])
  else:
    itinerary2[neighborids1] = itinerary[neighborids2]
    itinerary2[neighborids2] = itinerary[neighborids1]
  temperature=1/(time/(maxitin/10)+1)
  distance1 = howfar(genlines(cities,itinerary))
  distance2 = howfar(genlines(cities,itinerary2))
  itinerarytoreturn = itinerary.copy()
  scale = 3.5
#Мы хотим изменить это условие, чтобы готовность принять худший маршрут
#зависела не только от температуры, но и от того, насколько гипотетическое
# изменение ухудшает маршрут. Если ухудшение незначительно, то мы скорее
# примем его, чем значительную потерю. Для этого в условную команду будет
# включена метрика ухудшения маршрута scale
  if((distance2 > distance1 and (randomdraw) < (math.exp(scale*(distance1 - distance2)) * temperature)) or (distance1 > distance2)):
    itinerarytoreturn = itinerary2.copy()
  reset = True
#Отмена выполняется только в том случае, если мы опробовали много возмущений,
# но не добились улучшения по сравнению с предыдущим самым хорошим результатом  
  resetthresh = 0.04
#переменная resetthresh определит, как долго следует ожидать перед отменой
  if(reset and (time - minidx) > (maxitin * resetthresh)):
    itinerarytoreturn = minitinerary
    minidx = time
#Переменная minidx просто получает данные из time
  if(howfar(genlines(cities,itinerarytoreturn)) < mindistance):
    mindistance = howfar(genlines(cities,itinerary2))
    minitinerary = itinerarytoreturn
    minidx = time
#Переменная minidx просто получает данные из time
  if(abs(time - maxitin) <= 1):
    itinerarytoreturn = minitinerary.copy()
  return(itinerarytoreturn.copy())

# После всех правок и усовершенствований можно написать функцию siman()
# (сокращение от SIMulated ANnealing, то есть имитация отжига), которая
# создаст глобальные переменные, а затем многократно вызывает новейшую функцию
# perturb(), приведя к маршруту с очень малым расстоянием перемещения
def siman(itinerary,cities):
  newitinerary = itinerary.copy()
  global mindistance
  global minitinerary
  global minidx
  mindistance = howfar(genlines(cities,itinerary))
  minitinerary = itinerary
  minidx = 0
  maxitin = len(itinerary) * 1000
  for t in range(0,maxitin):
    newitinerary = perturb_sa3(cities,newitinerary,t,maxitin)
  return(newitinerary.copy())

np.random.seed(random_seed)
itinerary = list(range(N))
nnitin = donn(cities,N)
nnresult = howfar(genlines(cities,nnitin))
simanitinerary = siman(itinerary,cities)
simanresult = howfar(genlines(cities,simanitinerary))
print('Ближайший сосед', nnresult) #6.290
print('Оптимизир. Имитация отжига', simanresult) #5.438

plotitinerary(cities,simanitinerary,'Traveling Salesman Itinerary - Simulated Annealing','figure5')