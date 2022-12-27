spisok = '7,50,-43,9,-41,-23,16,-20,-38,16,-2,0,-19,24,40,-27,23,-39,49'
list_all = spisok.split(',')
list_p = []
list_o = []

for i in range(len(list_all)):
  if int(list_all[i]) > 0:
    list_p.append(list_all[i])
  elif int(list_all[i]) <= 0:
    list_o.append(list_all[i])
  else:
    print('Error!')

print('Список положительных чисел:\n',list_p)
print('Всего положительных: ', len(list_p))
print('Список отрицательных чисел:\n',list_o)
print('Всего отрицательных: ', len(list_o))