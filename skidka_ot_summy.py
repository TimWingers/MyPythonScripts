def skidka(pay_sum):
  print(f'Ваша сумма покупок составляет {pay_sum} руб')
  if pay_sum < 3000:
    print('На суммы до 3000 руб скидок нет')
  elif pay_sum >= 3000 and pay_sum < 5000:
    pay_sum = pay_sum - (pay_sum * 0.05)
    print('Ваша скидка составляет 5%')
    print(f'Сумма к оплате: {pay_sum} руб')
  elif pay_sum >= 5000 and pay_sum < 10000:
    pay_sum = pay_sum - (pay_sum * 0.07)
    print('Ваша скидка составляет 7%')
    print(f'Сумма к оплате: {pay_sum} руб')
  else:
    pay_sum = pay_sum - (pay_sum * 0.1)
    print('Ваша скидка составляет 10%')
    print(f'Сумма к оплате: {pay_sum} руб')