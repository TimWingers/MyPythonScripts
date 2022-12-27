# Алгоритм выражения дробей в виде непрерывных дробей
import math

def continued_fraction(x,y,length_tolerance):
  output = []      #создаем пустой список
  big = max(x,y)   #максимальное число среди x, y
  small = min(x,y) #минимальное число среди x, y
  while small > 0 and len(output) < length_tolerance:
    #пока наименьшее число больше 0 и длина списка меньше толерантного значения
    quotient = math.floor(big/small)  #делим нацело большее на меньшее
    output.append(quotient)  #присоедиеняем это число к списку
    new_small = big % small  #меняем наименьшее на целое деление big и small
    big = small              #присваиваем наибольшему старое наименьшее
    small = new_small        #присваиваем наименьшему новое наименьшее
  return(output)

result = continued_fraction(3050,13,200)
print(result)

# Преобразование непрерывной дроби в представление числа
def get_number(continued_fraction):
  index = -1
  number = continued_fraction[index]
  while abs(index) < len(continued_fraction):
    next = continued_fraction[index - 1]
    number = 1/number + next
    index -= 1
  return(number)

get_number(result)