def leap_year(x):
    long_years = list(range(4, 2496, 4))

    if x in long_years:
        print ('Високосный год')  
    else:
        print ('Не високосный год')

x = 2019
leap_year(x)


#2й способ
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('Високосный год')
else:
    print('Обычный год')