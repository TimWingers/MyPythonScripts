Capital = int(input('Каков размер твоего капитала? '))
ExchangeRate = 60
print("Твой текущий капитал " + str(Capital / ExchangeRate) + " долларов.")
print("Какая процентная ставка в банках? ", end="")
Percent = float(input())
Term = 0
while Capital < (1000000 * ExchangeRate) :
  Fee = Capital * Percent / 100
  Capital = Capital + Fee
  Term += 1
print("Чтобы стать долларовым миллионером, тебе понадобится ", end="")
print(str(Term) + " лет.")