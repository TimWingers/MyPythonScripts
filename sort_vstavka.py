#Сортировка методом вставки
cabinet = [720, 506, 187, 588, 841, 436, 286, 173, 583, 674, 37, 42, 911, 75, 91, 413, 819, 904, 498, 582, 653, 668, 961, 998, 441, 458, 208, 927, 751, 784, 862, 946, 881, 900, 506, 245, 67, 52, 535, 339]
def insertion_sort(cabinet):
  newcabinet = []
  while len(cabinet) > 0:
    to_insert = cabinet.pop(0)
    newcabinet = insert_cabinet(newcabinet, to_insert)
  return(newcabinet)
sortedcabinet = insertion_sort(cabinet)
print(sortedcabinet)