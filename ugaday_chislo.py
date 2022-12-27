#Генератор случаных чисел от 1 до 20
#Дает 5 попыток угадать число

import random
number = random.randint(1, 20)
max_tries = 5
tries = 0
print ('Угадайте число от 1 до 20. У вас 5 попыток ')
while tries < max_tries:
    guess = int(input('Напишите цифру: '))
    if guess < number:
        print('Загаданное число больше')
    elif guess > number:
        print('Загаданное число меньше')
    else:
        print('Вы победили!')
        break
    tries += 1
else: 
    print('Вы проиграли')
    print('Было загадано число:', number)