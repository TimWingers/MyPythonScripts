# Деревья принятия решений. 
# Поиск оптимальной точки разветвления.
# Сначала загружаем датасет
import pandas as pd
ess = pd.read_csv('ess.csv')
# Импортируем также библиотеку numpy
import numpy as np
# Попробуем разделить данные на ветви деревьев сначала грубым методом.
# Просто разделив диапазон на 2.
# Возьмем к примеру средний уровень счастья людей в зависимости
# от того насколько по шкале 10 они ведут активную социальную жизнь
social = list(ess.loc[:,'sclmeet'])
happy = list(ess.loc[:,'happy'])
low_social_happiness = [hap for soc,hap in zip(social,happy) if soc <= 5]
high_social_happiness = [hap for soc,hap in zip(social,happy) if soc > 5]
meanlower = np.mean(low_social_happiness)
meanhigher = np.mean(high_social_happiness)
print(meanlower)
print(meanhigher)
# 7.637945540767936
# 8.10521410165031
# Видим что данные отличаются даже при грубом подходе.
# Но как найти идеальную точку отсечения?

# Функция, находящая лучшую точку разбиения переменной для ветвления
# в дереве принятия решений 
def get_splitpoint(allvalues,predictedvalues):
  lowest_error = float('inf')
  best_split = None
  best_lowermean = np.mean(predictedvalues)
  best_highermean = np.mean(predictedvalues)
#переменная pctl (сокр. от percentile) используется для перебора всех чисел от 0 до 100 
  for pctl in range(0,100):
    split_candidate = np.percentile(allvalues, pctl)
#split_candidate определяет pct l-й процентиль данных
    loweroutcomes = [outcome for value,outcome in zip(allvalues,predictedvalues) if value <= split_candidate]
    higheroutcomes = [outcome for value,outcome in zip(allvalues,predictedvalues) if value > split_candidate]
    
    if np.min([len(loweroutcomes),len(higheroutcomes)]) > 0:
      meanlower = np.mean(loweroutcomes)
      meanhigher = np.mean(higheroutcomes)
# вычисляем средние оценки счастья асоциальных людей и социально активных людей 
# (meanlower и meanhigher соответственно)
    lowererrors = [abs(outcome - meanlower) for outcome in loweroutcomes]
    highererrors = [abs(outcome - meanhigher) for outcome in higheroutcomes]
    total_error = sum(lowererrors) + sum(highererrors)
# 3 строки выше это вычисление суммы ошибок. В нашем случае ошибка,
# интересующая нас, равна разности между прогнозируемой и фактической
# оценкой уровня счастья. Если дерево принятия решений прогнозирует, что уровень
# счастья равен 6, а на самом деле он равен 8, то ошибка дерева по отношению
# к оценке равна 2.
# Суммировав ошибки прогнозирования для каждого респондента
# в некой группе, можно получить суммарную ошибку, которая оценивает точность
# дерева принятия решений по прогнозированию счастья для участников группы.
# Чем ближе суммарная ошибка к нулю, тем лучше дерево
    if total_error < lowest_error:
      best_split = split_candidate
      lowest_error = total_error
      best_lowermean = meanlower
      best_highermean = meanhigher
# Если суммарная ошибка для этой точки разбиения меньше всех суммарных ошибок
# при использовании всех предыдущих кандидатов, то мы переопределяем переменную
# best_split равной split_candidate. После завершения цикла переменная best_split
# содержит точку разбиения, которая обеспечила наивысшую точность.
  return(best_split,lowest_error,best_lowermean,best_highermean)

# Эту функцию можно выполнить для любой переменной, как делается в следующем
# примере для hhmmb — переменной, в которой хранится количество членов семьи
# респондента
allvalues = list(ess.loc[:,'hhmmb'])
predictedvalues = list(ess.loc[:,'happy'])
print(get_splitpoint(allvalues,predictedvalues))
# (1.0, 60860.029867951016, 6.839403436723225, 7.620055170794695)
# Этот вывод можно интерпретировать так: для разбиения переменной hhmmb лучше
# всего использовать уровень 1.0; респонденты делятся на людей, живущих в
# одиночку (один член семьи), и живущих с другими (несколько членов семьи). 
# Также мы видим средние уровни счастья для этих двух групп: около 6.84 и 7.62
# соответственно.

# Функция перебирает все переменные и находит лучшую переменную
# для разбиения
def getsplit(data,variables,outcome_variable):
  best_var = ''
  lowest_error = float('inf')
  best_split = None
  predictedvalues = list(data.loc[:,outcome_variable])
  best_lowermean = -1
  best_highermean = -1

  for var in variables:
# for перебирает все переменные в списке переменных.
# Для каждой из них функция get_splitpoint() используется для нахождения
# лучшей точки разбиения    
    allvalues = list(data.loc[:,var])
    splitted = get_splitpoint(allvalues,predictedvalues)

  if(splitted[1] < lowest_error):
# Каждая переменная при разбиении по оптимальной точке приводит к некоторой
# суммарной ошибке в наших прогнозах
    best_split = splitted[0]
    lowest_error = splitted[1]
# Если некая переменная имеет более низкую сумму ошибки, чем все переменные,
# рассматриваемые ранее, то ее имя сохраняется в переменной best_var.    
    best_var = var
    best_lowermean = splitted[2]
    best_highermean = splitted[3]
# После перебора всех имен переменных будет найдена переменная с наименьшей
# суммой ошибки, хранящаяся в best_var
  generated_tree = [[best_var,float('-inf'),best_split,best_lowermean], 
  [best_var,best_split, float('inf'),best_highermean]]
  return(generated_tree)
##########################
variables = ['netusoft']  
outcome_variable = 'happy'
print(getsplit(ess,variables,outcome_variable))
#[['netusoft', -inf, 4.0, 7.647545995219832], ['netusoft', 4.0, inf, 7.95427337475375]]
# Функция getsplit() выводит очень простое «дерево» в формате вложенного
# списка касательно переменной доступа к Интернету. Оно состоит всего из 2 ветвей.
# netusoft <= 4 - это средний уровень счастья 7.6475..
# netusoft > 4 - это средний уровень счастья 7.9542..
# Таким образом мы можем сделать предварительный вывод что Интернет делает
# людей счастливее.