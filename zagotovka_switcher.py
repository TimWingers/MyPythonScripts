def switcher(param):
    def func1():
        print('Запускаю функцию 1')
        
    def func2():
        print('Запускаю функцию 2')
    
    if param == True:
        return func1()
    else:
        return func2()
    
switcher(True)
#Запускаю функцию 1