import requests
from bs4 import BeautifulSoup as BS4

r = requests.get("https://ru.wikipedia.org/wiki/Python")
# Получаем HTML-код
html = r.text

parser = BS4(html, "html.parser")
elements = parser.select("div#toc ul li a")

# Проходим по каждому элементу и забираем из него данные
for element in elements:
# Извлекаем текст из элемента
    title = element.getText()
# Извлекаем текст из атрибута href элемента
    link = element['href']
# Выводим на экран
    print(f"Заголовок: {title}, ссылка: {link}")

element = parser.select('p')
element[0].getText()