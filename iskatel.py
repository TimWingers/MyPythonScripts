#fruits = ['яблоко','груша','банан','киви','дерьмо','апельсин','арбуз']

def iskatel (list_name, what_to_find):
  if what_to_find in list_name:
    index = list_name.index(what_to_find)
    print(f'Значение <{what_to_find}> есть в списке')
    print(f'Его индекс <{index}>')
    choice = input('Удалить? (y/n) ')
    if choice == 'y':
      del list_name[index]
      print('Удалено')
  else:
    print('Такого значения в списке нет')

#iskatel(fruits, 'дерьмо')
#fruits