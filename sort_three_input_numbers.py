a = input('Enter a three digit positive number: ')
if len(a) == 3:
  lst = [a[0], a[1], a[2]]
  lst.sort(reverse = True)
  new_lst = ''.join(lst)
  print(new_lst)
else:
  print('This is not three digit positive number')



#Вторая версия. Без списков и встроенной сортировки
import random
a = str(random.randint(100, 999))
first_let = a[0]
second_let = a[1]
third_let = a[2]

if second_let > first_let and second_let > third_let and third_let > first_let:
  max_value = a[1];  med_value = a[2];  min_value = a[0]
elif second_let > first_let and second_let < third_let and third_let > first_let:
  max_value = a[2];  med_value = a[1];  min_value = a[0]
elif second_let > first_let and second_let > third_let and third_let < first_let:
  max_value = a[1];  med_value = a[0];  min_value = a[2]  
elif second_let < first_let and second_let < third_let and third_let > first_let:
  max_value = a[2];  med_value = a[0];  min_value = a[1]
elif second_let < first_let and second_let < third_let and first_let > third_let:
  max_value = a[0];  med_value = a[2];  min_value = a[1]
elif second_let == first_let and third_let > second_let:
  max_value = a[2];  med_value = a[1];  min_value = a[0]
elif second_let == third_let and first_let > second_let:
  max_value = a[0];  med_value = a[1];  min_value = a[2]
elif second_let == third_let and first_let < second_let:
  max_value = a[1];  med_value = a[2];  min_value = a[0]
elif third_let == first_let and second_let > first_let:
  max_value = a[1];  med_value = a[0];  min_value = a[2]
elif third_let == first_let and second_let < first_let:
  max_value = a[0];  med_value = a[2];  min_value = a[1]
else:
  max_value = first_let
  med_value = second_let
  min_value = third_let
print(max_value + med_value + min_value)