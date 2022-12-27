#Рассчитывает среднюю температуру по списку и переводит ее в Цельсии
import numpy as np
def avge_temp_fahr_cls(tdata):
    count = len(tdata)
    print('Средняя температура в странах: ')
    for i in range (count):
        geo = tdata[i][0] 
        avgtemp = ((np.mean(tdata[i][1]) - 32) * 5 / 9)
        print(f'{geo} - {avgtemp :.1f}C')
    
countries_temperature = [
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
tdata = countries_temperature
avge_temp_fahr_cls(tdata)