a = input('Enter a four digit positive number: ')
if len(a) == 4:
  b = a[3]+a[2]+a[1]+a[0]
  print(int(b))
else:
  print('This is not four digit positive number')



#2nd method
a = int(input('Enter a four digit positive number: '))
b = a % 10
if a >= 1000 and a <= 9999 and b != 0:
  a4 = a % 10
  a3 = a % 100 // 10
  a2 = a % 1000 // 100
  a1 = a % 10000 // 1000
  print(str(a4) + str(a3) + str(a2) + str(a1))
else:
  print('Error')