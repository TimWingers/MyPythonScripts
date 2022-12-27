import requests
def maxrate2ruble():
    load = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    dct = load.json()['Valute']
    max_v = 0
    max_k = ' '
    for key in dct:
        if dct[key]['Value'] > max_v:
            max_v = dct[key]['Value']
            max_k = key
    return max_k, max_v
maxrate2ruble()