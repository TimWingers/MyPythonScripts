# Алгоритм Имитация отжига (simulated annealing)
# Это измененная форма алгоритма поиска с возмущением. Принципиальное отличие
# заключается в том, что при имитации отжига мы иногда соглашаемся принять
# изменения маршрута, увеличивающие преодолеваемое расстояние, поскольку это
# позволяет обойти проблему локальной оптимизации. Наша готовность к принятию
# худших маршрутов зависит от текущей температуры

# Температурная функция.
# Максимальный риск на оптимизацию вначале, минимальный - в конце
import matplotlib.pyplot as plt
# Зададим температурную функцию
temperature = lambda t: 1/(t + 1)
ts = list(range(0,100)) #переменная содержащая диапазон значений t от 1 до 100
# Построим график
plt.plot(ts, [temperature(t) for t in ts])
plt.title('The Temperature Function')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.show()

# Обновленная версия функции perturb(), которая учитывает температуру
# и случайный фактор

def perturb_sa1(cities,itinerary,time):
#появится новый аргумент: время time. Он определяет, насколько мы
# продвинулись в процессе имитации отжига.
# первый вызов perturb() начинается с времени 1, после чего время будет
# равно 2, 3 и т. д., в зависимости от того, сколько раз вызывается функция perturb() 
  neighborids1 = math.floor(np.random.rand() * (len(itinerary)))
  neighborids2 = math.floor(np.random.rand() * (len(itinerary)))
  itinerary2 = itinerary.copy()
  itinerary2[neighborids1] = itinerary[neighborids2]
  itinerary2[neighborids2] = itinerary[neighborids1]
  distance1 = howfar(genlines(cities,itinerary))
  distance2 = howfar(genlines(cities,itinerary2))
  itinerarytoreturn = itinerary.copy()
  randomdraw = np.random.rand() #добавим строку где выбирается случайное число
  temperature = 1/((time/1000) + 1) #добавим строку, которая задает температурную функцию
  if((distance2 > distance1 and (randomdraw) < (temperature)) or (distance1 > distance2)):
    itinerarytoreturn=itinerary2.copy()
#Если случайное число меньше температуры, то мы будем готовы принять ухудшенный
# маршрут. Если случайное число больше температуры, то ухудшенный маршрут
# приниматься не будет     
  return(itinerarytoreturn.copy())

#Сравнение эффективности имитации отжига с другими алгоритмами поиска
itinerary = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,\
26,27,28,29,30,31,32,33,34,35,36,37,38,39]
np.random.seed(random_seed)

itinerary_sa = itinerary.copy()
for n in range(0,len(itinerary) * 500):
  itinerary_sa = perturb_sa1(cities,itinerary_sa,n)

print('Случайный маршрут', howfar(genlines(cities,itinerary))) #16.808
print('Поиск с возмущением', howfar(genlines(cities,itinerary_ps))) #7.379 
print('Имитация отжига', howfar(genlines(cities,itinerary_sa))) #13.145 
print('Ближайший сосед', howfar(genlines(cities,donn(cities,N)))) #6.290