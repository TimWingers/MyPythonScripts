# Тест на случайность чисел. Тест пересекающихся сумм.
# Берет весь список случайных чисел и вычисляет суммы последовательных
# элементов списка. Набор таких сумм должен следовать колоколообразной
# закономерности или гауссовой кривой.
import matplotlib.pyplot as plt

def overlapping_sums(the_list,sum_length): #передаем список и его длину
  length_of_list = len(the_list)  #присваиваем переменной значение длины списка
  the_list.extend(the_list)  #расширение списка за счет старого списка
  output = []                #создаем пустой массив
  for n in range(0,length_of_list):  #пробегаемся по нему от 0 до длины
    output.append(sum(the_list[n:(n + sum_length)]))
    #присоединяем к массиву сумму списка по формуле
  return(output)

overlap = overlapping_sums(list_random(211111,111112,300007),12)
plt.hist(overlap, 20, facecolor = 'blue', alpha = 0.5)
plt.title('Results of the Overlapping Sums Test')
plt.xlabel('Sum of Elements of Overlapping Consecutive Sections of List')
plt.ylabel('Frequency of Sum')
plt.show()

overlap = overlapping_sums(list_random(29,23,32),32)
plt.hist(overlap, 20, facecolor = 'blue', alpha = 0.5)
plt.title('Results of the Overlapping Sums Test')
plt.xlabel('Sum of Elements of Overlapping Consecutive Sections of List')
plt.ylabel('Frequency of Sum')
plt.show()