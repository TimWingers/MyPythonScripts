import requests
API_URL = 'https://api-metrika.yandex.ru/stat/v1/data'
METRIKA_ROWS_LIMIT = 5  # max 100000

DEMO_COUNTER = 44147844
class Metrika:
    def __init__(self, token='', counter=DEMO_COUNTER, start_date='2020-09-01', end_date='2020-09-10'):
        self.counter = counter
        self.limit = METRIKA_ROWS_LIMIT
        self.start_date = start_date
        self.end_date = end_date
        
        if token:
            self.headers = {'Authorization': 'OAuth ' + token}
        else:
            self.headers = ''  # для демо-счетчика заголовок запроса должен быть пустым
        
        self.dimensions = ''
        self.metrics = ''
        self.report = []
        
    def api_request(self, offset=1):
        """Запрос к API Метрики, возвращает словарь с отчетом"""
        params = {
            'id': self.counter,
            'date1': self.start_date,
            'date2': self.end_date,
            'metrics': self.metrics,
            'dimensions': self.dimensions,
            'limit': self.limit,
            'offset': offset,
            'accuracy': 1,
        }
        
        response = requests.get(API_URL, params=params, headers=self.headers)
        return response.json()['data']
    
    def traffic(self):
        """Отчет по посещаемости"""
        self.metrics = 'ym:s:visits'
        self.dimensions = 'ym:s:date'
        
        # report = self.api_request()
        report = self.full_report()
        self.report = report
        
    def browser(self):
        """Отчет по посещаемости"""
        self.metrics = 'ym:s:visits'
        self.dimensions = 'ym:s:date,ym:s:browser'
        
        # report = self.api_request()
        report = self.full_report()
        self.report = report
    
    def reformat_api_report(self):
        """Упрощение отчета до списка списков"""
        reformatted_report = []

        for line in self.report:
            dimensions = [x['name'] for x in line['dimensions']]
            reformatted_report.append(dimensions + line['metrics'])

        self.report_formatted = reformatted_report
    
    def full_report(self):
        """Постраничная выгрузка из Метрики"""
        full_data = []
        offset = 1
        
        while True:
            print('Starting offset {}'.format(offset))
            data = self.api_request(offset=offset)
            full_data += data
            
            offset += self.limit
            if not data or len(data) < self.limit:
                break
        
        return full_data
    
    
m = Metrika(start_date='2022-11-01', end_date='2022-12-21')
m.traffic()