class BankAccount:   #создаем класс Банковский счет
  def __init__(self, acct_number, acct_name): #инициализируем параметры класса
    self.acct_number = acct_number
    self.acct_name = acct_name
    self.balance = 0.00   #изначальный баланс счета равен 0
  
  def displayBalance(self):  #функция показа баланса
    print ("На вашем счету:", round(self.balance, 2))
    
  def deposit(self, amount): #функция пополнения счета
    self.balance = self.balance + amount  #прибавляем amount к балансу
    print ("Вы положили", amount)
    print ("Теперь на вашем счету:", round(self.balance, 2))

  def withdraw(self, amount): #функция снятия денег со счета
    if self.balance >= amount:  #проверяем достаточно ли денег на счете
      self.balance = self.balance - amount  #уменьшаем баланс на сумму снятия
      print ("Вы сняли", amount)
      print ("Теперь на вашем счету:", round(self.balance, 2))
    else:                       #иначе (если денег на счету недостаточно)
      print ("Вы попытались снять", amount)
      print ("На вашем счету:", round(self.balance, 2))
      print ("В операции отказано. Недостаточно средств.")
#Теперь пишем код для конкретного клиента
clients_database = {234567: 'Дмитрий Крылов'}
client_name = clients_database [234567]  #Вытаскиваем имя из словаря
Account234567 = BankAccount(234567, client_name) #Создаем переменную
print (f'Здравствуйте {Account234567.acct_name}!')
print ('Добро пожаловать в наш интернет-банк')
print ('Ваш номер счета:', Account234567.acct_number)
Account234567.displayBalance()          #Выводим текущий баланс

while True:   #пока клиент не откажется, позволяем ему работать
  print()
  add_or_withdraw = input('Желаете пополнить или снять сумму? (a/w) ')
  if add_or_withdraw == 'a':
    dep_sum = float(input('Введите сумму пополнения (напр. 10.00): '))
    Account234567.deposit(dep_sum)  #аналогично Account234567.deposit(10.00)
    more_operations = input('Будут ли еще операции сегодня? (y/n) ')
    if more_operations == 'n':
      print ('Всего доброго! Будем рады вас видеть снова.')
      break
  if add_or_withdraw == 'w':
    wit_sum = float(input('Введите сумму снятия со счета (напр. 10.00): '))
    Account234567.withdraw(wit_sum) #аналогично Account234567.withdraw(10.00)
    more_operations = input('Будут ли еще операции сегодня? (y/n) ')
    if more_operations == 'n':
      print ('Всего доброго! Будем рады вас видеть снова.')
      break  