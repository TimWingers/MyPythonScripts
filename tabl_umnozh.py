num = int(input('Для какого числа нужна таблица умножения? '))
mnoz = int(input('До какого множителя вы хотите дойти? '))

print('Вот ваша таблица: ')
for x in range(1, mnoz+1):
  mult = num * x
  print(f'{num} x {x} = {mult}') 