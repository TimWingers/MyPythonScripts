import json
# Строка с JSON-объектом
json_string = '{"name":"Oleg","age":19,"country":"Russia","city":{"1":1,"2":2,"3":3,"4":4}}'
# Декодируем строку для работы с Python
dec_json = json.loads(json_string)
# Выводим тип объекта, который получился при десериализации
print(type(dec_json))
# Выводим сам объект и его структуру в виде строки
print(dec_json)