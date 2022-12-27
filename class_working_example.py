class MyFriend:
# Переменная (свойство)
    name = None
# Конструктор
    def __init__(self, name):
        self.name = name
# Функция (метод)
    def say_hello(self):
        print(f"Hello {self.name}")
# Функция (метод)
    def say_goodbye(self):
        print(f"Goodbye {self.name}")
# Функция (метод)
    def say_whats_going(self):
        print(f"What`s going {self.name}?")

friend = MyFriend()
friend.name = "Korben"
friend.say_hello()
friend.say_goodbye()
friend.say_whats_going()