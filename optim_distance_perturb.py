# Алгоритм поиска с возмущениями.
# Функция, которая вносит небольшое изменение в маршрут,
# сравнивает измененный маршрут с исходным и возвращает более короткий маршрут
def perturb(cities,itinerary):
#получаем в аргументах произвольный список городов и маршрут 
  neighborids1 = math.floor(np.random.rand() * (len(itinerary)))
  neighborids2 = math.floor(np.random.rand() * (len(itinerary)))
# Определяем две переменные, случайно выбранные целые числа в диапазоне
# от 0 до длины маршрута
  itinerary2 = itinerary.copy()
# Затем создается новый маршрут itinerary2, который идентичен исходному,
# не считая того, что города neighborids1 и neighborids2 меняются местами
  itinerary2[neighborids1] = itinerary[neighborids2]
  itinerary2[neighborids2] = itinerary[neighborids1]
#вычисляем distance1 — общее расстояние исходного маршрута 
  distance1 = howfar(genlines(cities,itinerary))
#вычисляем distance2 — общее расстояние маршрута itinerary2 
  distance2 = howfar(genlines(cities,itinerary2))
  itinerarytoreturn = itinerary.copy()
  if(distance1 > distance2):
# Если distance2 меньше distance1, то возвращается новый маршрут (с заменой городов)
    itinerarytoreturn = itinerary2.copy()
  return(itinerarytoreturn.copy())
# В противном случае возвращается исходный маршрут.
# Таким образом, этой функции передается маршрут, а она всегда 
# возвращает маршрут как минимум не хуже переданного

itinerary = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,\
26,27,28,29,30,31,32,33,34,35,36,37,38,39]

np.random.seed(random_seed)
itinerary_ps = itinerary.copy()
for n in range(0,len(itinerary) * 500):
  itinerary_ps = perturb(cities,itinerary_ps)

print(howfar(genlines(cities,itinerary_ps)))
# 7.37 - оптимизация маршрутов более чем на 50% по сравнению со случайным подбором