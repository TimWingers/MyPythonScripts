def monets (x1, x2, x3, x4):
  y1 = x1 * 1
  y2 = x2 * 5
  y3 = x3 * 10
  y4 = x4 * 50
  total = y1 + y2 + y3 + y4
  return total

x1 = int(input('Сколько у вас монет 1 коп?: '))
x2 = int(input('Сколько у вас монет 5 коп?: '))
x3 = int(input('Сколько у вас монет 10 коп?: '))
x4 = int(input('Сколько у вас монет 50 коп?: '))
kopilka_sum = monets(x1, x2, x3, x4)
kopilka_rub = kopilka_sum / 100
print(f'В вашей копилке всего: {kopilka_sum} копеек или {kopilka_rub} рублей')  