# 75  29  13
benzobak = int(input('Емкость бензобака в литрах? '))
benzin = int(input('Сколько топлива в баке в литрах? '))
rashod = int(input('Сколько литров тратит ваш а/м на 100 км? '))
do_zapravki = 200

real_rashod = rashod * 1.05  #на погрешность датчика топлива, возможные пробки
zapoln = (benzin / benzobak) * 100
proehat1 = round((benzin / rashod) * 100)
proehat2 = round((benzin / real_rashod) * 100)

print(f'Объем бензобака: {benzobak} литров')
print(f'Заполненность топливом: {zapoln} %')
print(f'Ваш авто тратит {rashod} л на 100 км')
print(f'Вы можете проехать еще от {proehat2} до {proehat1} км')
print(f'Следующая заправка через {do_zapravki} км')

if proehat2 > do_zapravki:
  print('Можно не заправляться сейчас и доехать до следующ. заправки')
else:
  print('Надо заправить машину сейчас! Иначе закончится бензин!')