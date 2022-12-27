#Суммирует введенные пользователем числа пока он не выберет 0
def summator():
    num = int(input('Введите число: '))
    box = []
    while num != 0:
        box.append(num)
        num = int(input('Введите число: '))
    else:
        print('Результат: ', sum(box))
        
summator()


#2й метод
number = True
sum_ = 0
while number != 0:
   number = int(input('Введите число '))
   sum_ += number
print(sum_)