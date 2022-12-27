from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class SMTPClient:
    def __init__(self, login, password, host="smtp.gmail.com", port=587):
# Инициализируем логин и пароль от SMTP-сервера
        self.__login, self.__password = login, password
# Создадим объект SMTP-сервера
        self.__smtp_server = smtplib.SMTP(host, port)
        self.__smtp_server.starttls()
        
    def __make_msg(self, subject, message, email):
# Инициализируем объект сообщения, которое будет отправлено пользователю
        self.__msg = MIMEMultipart()
# От кого. Указываем наш емейл от гугла
        self.__msg['From'] = self.__login
# Кому. Указываем адрес пользователя, которому будет отправлено сообщение
        self.__msg['To'] = email
# Тема. Заголовок сообщения
        self.__msg['Subject'] = subject
# Текст сообщения пропущенный в виде специального объекта
        self.__msg.attach(MIMEText(message, 'plain'))
        
    def __send_message(self, subject, message, email):
# Создаём сообщение для отправки
        self.__make_msg(subject, message, email)
# Авторизуемся на сервере
        self.__smtp_server.login(self.__login, self.__password)
# Отправляем сообщение
        self.__smtp_server.sendmail(self.__msg['From'], self.__msg['To'], self.__msg.as_string())
        print(f"Отправили сообщение по адресу: {email}")
        
    def send_messages(self, subject, message, emails):
        try:
            for email in emails:
                self.__send_message(subject, message, email)
        finally:
# Закрываем соединение с сервером
            self.__smtp_server.quit()
    
# Список емейлов для рассылки
emails = ["mail1@rambler.ru", "mail2@rambler.ru", "mail3@lenta.ru"]
# Создаём объект клиента
SMTPClient = SMTPClient("mymail@gmail.com", "mypass")
# Отправляем сообщение
SMTPClient.send_messages("Заголовок сообщения", "Текст сообщения", emails)