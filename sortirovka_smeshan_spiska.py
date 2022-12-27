#Допустим имеем смешанный список. Как его отсортировать?
lst = [1,3,-10,[],'a','abc',2,9.0,[1,-2],'opr',[0,5,6]]
#Разделим его на три списка (1 для чисел, 1 для строк, 1 для влож. списков)
lst_num = []
lst_str = []
lst_list = []
#Распределение элементов по трем категориям
for i in range(len(lst)):    #для каждого индекса в старом списке
  if type(lst[i]) == int or type(lst[i]) == float:  #если видим числа
    lst_num.append(lst[i])   #добавляем в новый список для чисел
  elif type(lst[i]) == str:  #если видим символы
    lst_str.append(lst[i])   #добавляем в новый список для строк
  elif type(lst[i]) == list: #если у нас вложенный список    
    lst_list.append(lst[i])  #добавляем в новый список для списков
#Сортируем образованные 3 списка
lst_num.sort()
lst_str.sort()
lst_list.sort()
#склеиваем (конкатенируем) полученные списки
new_lst = lst_num + lst_str + lst_list
#И выводим объединенный новый список на экран
print(new_lst) #[-10, 1, 2, 3, 9.0, 'a', 'abc', 'opr', [], [0,5,6], [1,-2]]