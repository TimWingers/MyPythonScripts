a = input('Enter a four digit positive number: ')
if len(a) == 4:
  first_half_sum = int(a[0]) + int(a[1])
  second_half_sum = int(a[2]) +int(a[3])
  if first_half_sum == second_half_sum:
    print('This is happy ticket!')
  else:
    print('This is not happy ticket')
else:
  print('This is not four digit positive number')



 #Second method
a = int(input('Enter a four digit positive number: '))
if a >= 1000 and a <= 9999:  #допустим 3764
  a4 = a % 10                #получаем 4
  a3 = a % 100 // 10         #получаем 6
  a2 = a % 1000 // 100       #получаем 7
  a1 = a % 10000 // 1000     #получаем 3
  if (a4 + a3) == (a1 + a2): #сравниваем суммы
    print('This is happy ticket!')
  else:
    print('This is not happy ticket!')
else:
  print('Error')


#Third method (for 6 digits and in function)
def happy_ticket (a):
    if a >= 100000 and a <= 999999:
        a6 = a % 10                
        a5 = a % 100 // 10         
        a4 = a % 1000 // 100       
        a3 = a % 10000 // 1000     
        a2 = a % 100000 // 10000    
        a1 = a % 1000000 // 100000     
        if (a4 + a5 + a6) == (a1 + a2 + a3):
            print('Счастливый билет')
        else:
            print('Несчастливый билет')
    else:
        print('Ошибка!')

a = int(input('Введите шестизначное положительное число: '))
happy_ticket(a)