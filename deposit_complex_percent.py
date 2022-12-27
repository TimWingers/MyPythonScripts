def complex_percent (deposit_sum, year_rate, period_months):
  period_year = period_months / 12
  withdraw_sum = deposit_sum * (pow((1 + year_rate / period_months), period_months * period_year))
  profit = withdraw_sum - deposit_sum
  roi = ((withdraw_sum - deposit_sum) / deposit_sum * 100)
  print (f'Withdraw sum after {period_months} months is {withdraw_sum:.2f}')
  print (f'Your profit: {profit:.2f}')
  print (f'Return on investment: {roi:.2f}%')
#Закладываем параметры (1 млн под 7% на 36 месяцев)
complex_percent (1000000, 0.07, 36)