#Выводит одну среднюю букву для слов с нечетным числом букв
#или 2 средние буквы для слов с четным числом.
def medium_letter(string):
    if len(string) % 2 != 0:
        med = len(string) // 2
        return string[med]
    else:
        med1 = len(string) // 2 - 1
        med2 = len(string) // 2 + 1
        return string[med1:med2]

string = 'testing'
medium_letter(string) 


#2й метод
word = 'testing'
print(word [ (len(word)-1)//2 : (len(word)+2)//2 ])