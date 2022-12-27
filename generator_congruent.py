# Генерация (псевдо) случайных чисел
# Линейный конгруэнтный генератор

def next_random(previous,n1,n2,n3):
  the_next = (previous * n1 + n2) % n3
  return(the_next)

next_random(5,734,345,234)  #37 (и будет всегда 37 с таким кортежем)

# Функция генерации нескольких псевдослучайных чисел
def list_random(n1,n2,n3):
  output = [n1]  #первое значение в списке
  while len(output) <=n3:  #пока длина списка меньше n3
   output.append(next_random(output[len(output) - 1],n1,n2,n3))
   #добавить в список значение из предыд.функции
  return(output)

print(list_random(29,23,32))
print(list_random(1,18,36))
print(list_random(1,1,37))