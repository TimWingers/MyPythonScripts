a = input('Введите целые числа через пробел: ')
list_all = a.split()
list1 = []
list2 = []

for i in range(len(list_all)):
  if int(list_all[i]) % 2 == 0:
    list1.append(list_all[i])
  else:
    list2.append(list_all[i])
print('Список четных чисел:\n',list1)
print('Список нечетных чисел:\n',list2)