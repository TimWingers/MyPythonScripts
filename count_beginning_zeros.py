#Считает число нулей в начале строки
def count_beginning_zeros(a):
    b = (f'{int(a)}')
    return len(a) - len(b) if int(a) != 0 else len(a)

count_beginning_zeros("00001")