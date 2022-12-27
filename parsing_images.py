import shutil
import requests
import urllib.parse
from bs4 import BeautifulSoup as BS4


def get_page(phrase, page):
# Определяем ссылку на страницу, к которой будем отправлять запрос
    link = "https://www.istockphoto.com/" + phrase
# Определяем словарь с заголовками
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
# Определяем словарь с параметрами запроса
    params = {"page": page, "phrase": phrase, "sort": "mostpopular"}
# Отправляем запрос на страницу с картинками
    request = requests.get(link, headers=headers, params=params)
# Возвращаем HTML-код из функции
    return request.text


# Проверяет, есть ли на странице изображения
def is_404(html):
    page = BS4(html, "html.parser")
# Если на странице ни одного изображения - возвращаем True
    if len(page.select("img.gallery-asset__thumb")) < 0:
        return True
    return False


# Получает список ссылок с конкретной страницы из выдачи по запросу
def get_imgs_from_page(phrase, page):
# Получаем HTML-код конкретной страницы выдачи
    html = get_page(phrase, page)
# Определяем локальный список, в который будут помещаться ссылки на изображение
    images = []
# Если вернуло страницу 404, значит прерываем выполнение функции, возвращая False
    if is_404(html) == True:
        return False
# Загружаем код страницы полученной с сервера в парсер
    img_node = BS4(html, "html.parser")
# Извлекаем все элементы со ссылками на картинки
    imgs = img_node.select("img.gallery-asset__thumb")
# Извлекаем из элементов ссылки на картинки и добавляем их в список
    for img in imgs:
        if img.has_attr("src"):
            print(f"Получили ссылку на фото: {img['src']}")
            images.append(img["src"])
# Возвращаем список из функции
    return images


# Получает список ссылок на изображения с заданного количества страниц по запросу
def get_images(query, pages):
# Переводим ключевой запрос в приемлемый формат
    query = urllib.parse.quote(query)
# Создаём список, в который будут помещаться все ссылки
    images = []
# Запускаем цикл, для парсинга по страницам
    for i in range(pages):
# Так как цикл начинается с 0, определяем номер страницы
        num_of_page = i + 1
# Получаем все изображения со страницы
        img = get_imgs_from_page(query, num_of_page)
# Если в переменной False, значит больше страниц с
# фотографиями нет прерываем цикл
        if not img:
            break
        else:
            images += img
    return images


result = get_images("BMW", 2)
print(f"Получили ссылки на: {len(result)} фотографий")

# Скачивает все изображения по запросу в заданную папку
def download_images(folder, phrase, page):
# Получаем все ссылки из выдачи по запросу
    images = get_images(phrase, page)
# Сохраняем все ссылки
    for image in images:
# Запускаем функцию сохранения в
        try:
            save_image(folder, image)
        except Exception as error:
            print(f"Проблема с записью файла: {error}")

download_images("C:/Users/Moneymaker/Desktop/img", "money", 2)