#fruits = ['яблоко','груша','банан','киви','дерьмо','апельсин','арбуз']

def zamenitel (list_name, what_to_delete, what_to_add):
  index = list_name.index(what_to_delete)
  del list_name[index]
  list_name.insert(index, what_to_add)

#zamenitel(fruits, 'дерьмо', 'манго')
#fruits