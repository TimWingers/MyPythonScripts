import requests
from bs4 import BeautifulSoup as BS4

class PageParser:
# Определяем базовый адрес сайта
    __base_url = "http://www.smartphone.ua"
    
    def __get_count_of_pages(self):
# Получаем код страницы с новостями
        page = requests.get(f"{self.__base_url}/news/")
# Если страница доступна
        if page.status_code == 200:
# Создаём объект парсера исходного кода страницы
            html_parser = BS4(page.text, "html.parser")
# Получаем ссылку на последеюю страницу из выдачи
            page_element = html_parser.select("div.pages a.digit")[-1]
# Получаем номер страницы из ссылки
            count_of_pages = page_element.getText()
# Возвращаем номер страницы с типом int
            return int(count_of_pages)
        return 0

    def __get_news_from_page(self, num_of_page):
        try:
# Получаем исходный код страницы из выдачи
            page = requests.get(f"{self.__base_url}/news/_page{num_of_page}.html")
# Если страница доступна
            if page.status_code == 200:
# Создаём объект парсера для этой страницы
                html_parser = BS4(page.text, "html.parser")
# Возвращаем список ссылок со страницы
                return html_parser.select("ul#news_list a.green")
# В противном случае
            else:
# Возвращаем пустой список
                return []
# Если при парсинге возникла ошибка
        except:
# Возвращаем пустой список
            return []

    def get_news(self):
# Получаем список страниц, и прибавляем единицу
        count_of_pages = self.__get_count_of_pages() + 1
# Определяем список для ссылок на новости
        news_list = []
# Проходим в списке все страницы выдачи
        for i in range(1, count_of_pages):
# У каждой страницы получаем ссылки на новости и добавляем
# их в список news_list
            [news_list.append(f"{self.__base_url}{news['href']}") for news in self.__get_news_from_page(i)]
# Возвращаем список news_list
        return news_list

class ExternalLinksParser:
    def __init__(self, list_of_news):
# Инициализируем список ссылок на новости
        self.__list_of_news = list_of_news
    
    def __is_external_link(self, link):
# Если ссылка начинается с символа "/"
# значит это внутренняя ссылка
        if link.startswith("/"):
            return False
# Если ссылка начинается с символа "#"
# значит это внутренняя ссылка
        if link.startswith("#"):
            return False
# Если ссылка содержит имя сайта
# значит это внутренняя ссылка
        if "smartphone.ua" in link:
            return False
# В остальных случаях - это внешняя ссылка
        return True

    def __get_links_from_page(self, link):
# Определяем список для ссылок
        links = []
        try:
# Отправляем запрос к странице
            page = requests.get(link)
# Если страница доступна
            if page.status_code == 200:
# Создаём объект парсера этой страницы
                html_parser = BS4(page.text, "html.parser")
# Получаем все элементы со ссылками
                list_of_links = html_parser.select("a")
# Добавляем ссылка в список inks
                [links.append(link["href"]) for link in list_of_links]
# Возвращаем список
                return links
# Иначе, если страница недоступна
# возвращаем пустой список
            return []
# Если возникла ошибка
        except:
# Возвращаем пустой список
            return []

    def __get_external_links_from_page(self, link):
# Определяем список для внешних ссылок
        external_links = []
# Получаем все ссылки со страницы
        links = self.__get_links_from_page(link)
# Если текущая ссылка внешняя, тогда добавляем её в список external_links
        [external_links.append(link) for link in links if self.__is_external_link(link)]
# Возвращаем список со внешними ссылками
        return external_links

    def get(self):
# Определяем список для внешних ссылок
        external_links = []
# Проходим в цикле каждую ссылку на новость
        for news_link in self.__list_of_news:
# Извлекаем из каждой новости внешние ссылки
            ex_links = self.__get_external_links_from_page(news_link)
# Добавляем все ссылки из новости в список external_links
            [external_links.append(ex_link) for ex_link in ex_links]
# Возвращаем список без дублей
        return list(set(external_links))

import socket

class DomainChecker:
    def __this_domain_is_available(self, link):
        try:
            print(f"Проверяем домен: {link}")
    # Если сокет не выбросил ошибку,
    # значит домен занят
            socket.gethostbyname_ex(link)
    # Если ошибка была выброшена,
    # значит домен свободен
        except:
            return True
        return False

    def __make_clear_domain(self, url):
    # Извлекаем только ност: vk.com,
    # вместо https://vk.com/
        first = url.split("/")[2]
        return first

    def __make_uniq_domains(self, links):
    # Определяем список для
    # неповторяющихся доменов
        clear_links = []
    # Проходим все ссылки в цикле
        for link in links:
    # Извлекаем из ссылки хост
            clear_links.append(self.__make_clear_domain(link))
    # Возвращаем очищенный от дублей список ссылок
        return list(set(clear_links))

    def check(self, links):
    # Определяем список для свободных доменов
        available_domains = []
    # Получаем список уникальных хостов
        links = self.__make_uniq_domains(links)
    # Проходим по списку хостов в цикле
        for link in links:
    # Если хост свободен
            if self.__this_domain_is_available(link):
                print(f"Домен свободен: {link}")
    # Добавляем его в список свободных доменов
                available_domains.append(link)
            else:
                print(f"Домен занят: {link}")
    # Возвращаем список свободных доменов
        return available_domains

# Объект парсера новостей сайта
page_parser_obj = PageParser()
# Список ссылок на новости сайта
news_links = page_parser_obj.get_news()
# Объект парсера внешних ссылок
external_links_obj = ExternalLinksParser(news_links)
# Список внешних ссылок
external_links = external_links_obj.get()
# Объект чекера доменов
domain_checker_obj = DomainChecker()
# Список свободных доменов
free_domains = domain_checker_obj.check(external_links)
# Выводим свободные домены на экран
print(free_domains)