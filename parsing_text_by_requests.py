import requests

# Устанавливаем переменную с юзерагентом
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
# Создаём словарь заголовков, передаём в гено юзерагент
headers = {"user-agent": user_agent}
# Формируем ссылку
link = "https://ru.wikipedia.org/wiki/Python"
# Отправляем запрос
r = requests.get(link, headers=headers)

# Получаем HTML-код страницы:
html = r.text

# Создаём новый файл
with open("article.html", "w", encoding="utf-8") as f:
# Записываем HTML-код в файл
    f.write(html)