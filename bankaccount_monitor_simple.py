class BankAccount:
  def __init__(self, name, id, money):
    self.name = name
    self.id = id
    self.money = money
  def __str__(self): 
    msg = "Привет, " + str(self.name) + ". На вашем счету " + str(self.id) + " лежит " + str(self.money) + " рублей."
    return msg

myAccount = BankAccount("Петр Петрович", "00128579", 154500)
print (myAccount)