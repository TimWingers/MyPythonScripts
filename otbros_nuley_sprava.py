def no_boring_zeros(n):
    if (n == 0) or (n % 10 != 0):
        return n
    else:
        a = str(n)  #переводим числов в строку
        b = a.rstrip('0')  #убираем нули справа у строки
        c = int(b)      #снова переводим строку в число
        print (c)
    
no_boring_zeros(-906000)


#2nd method
def no_boring_zeros(n):
    if n == 0:
        return n
    while n % 10 == 0:
        n = n / 10  #-90600.0 > -9060.0 > -906.0
    return int(n)

no_boring_zeros(-906000)