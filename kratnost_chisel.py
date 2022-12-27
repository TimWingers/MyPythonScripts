a = input('Список чисел которые нужно проверить на кратность (через","): ')
b = int(input('Кратность какому числу будем проверять: '))
list_all = a.split(',')
list1 = []
list2 = []

for i in range(len(list_all)):
  if int(list_all[i]) // b != 0 and int(list_all[i]) % b == 0:
    list1.append(list_all[i])
  else:
    list2.append(list_all[i])

print(f'Числа, кратные {b}:\n',list1)
print('Все остальные числа:\n',list2)