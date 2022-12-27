import re
def validator_car_id(car_ids):
    regexp = re.compile(r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}(?P<reg>\d{2,3})$')
    for id in car_ids:
        match = regexp.match(id)
        if match:
            print(f'Результат: Номер {id} валиден. Регион: {match["reg"]}')
        else:
            print(f'Результат: Номер {id} не валиден')
        
car_ids = ['А222ВС96', 'АБ22ВВ193']
validator_car_id(car_ids)