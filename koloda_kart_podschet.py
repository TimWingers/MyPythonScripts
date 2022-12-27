#pip install cards  - устанавливаем модуль cards (если необходимо)
#Импортируем нужные библиотеки
import random
from cards import Card
#Определяем класс для карт в колоде
class Card:  
  def __init__(self, suit_id, rank_id):
    self.rank_id = rank_id   #создаем атрибут достоинства карт
    self.suit_id = suit_id   #создаем атрибут масти карт
#Определяем достоинства карт (2,3,4,5 итд)  
    if self.rank_id == 1:
      self.rank = "Ace"
      self.value = 1
    elif self.rank_id == 11:
      self.rank = "Jack"
      self.value = 10
    elif self.rank_id == 12:
      self.rank = "Queen"
      self.value = 10
    elif self.rank_id == 13:
      self.rank = "King"
      self.value = 10
    elif 2 <= self.rank_id <= 10:  #если карта от 2 до 10, то ее ранг такой же
      self.rank = str(self.rank_id)
      self.value = self.rank_id
    else:
      self.rank = "RankError"  #Проверяем ошибки (попал ли rank_id в корр.диапазон, является ли int)
      self.value = -1
#Определяем масти карт
    if self.suit_id == 1:
        self.suit = u'\u2666'  #бубны
    elif self.suit_id == 2:
      self.suit = u'\u2665'    #черви
    elif self.suit_id == 3:
      self.suit = u'\u2660'    #пики
    elif self.suit_id == 4:
      self.suit = u'\u2663'    #трефы
    else:
      self.suit = "SuitError"  #Проверяем ошибки (попал ли suit_id в корр.диапазон, является ли int)
#Создаем короткое имя каждой карте (например 4♥) 
    self.short_name = self.rank[0] + self.suit[0]
    if self.rank == '10':
      self.short_name = self.rank + self.suit[0]

#Создаем колоду карт
deck = []  #начинаем с пустого списка
for suit_id in range(1, 5):  #генерируем для 4 мастей
  for rank_id in range(1, 14):  #13 разных достоинств
    deck.append(Card(suit_id, rank_id))  #и присоединяем их всех к списку

#Вытаскиваем случайные карты из колоды
hand = []  #начальное состояние колоды
for cards in range(0, 25): #допустим сдано 25 карт
  a = random.choice(deck)  #случайным образом из колоды
  hand.append(a)           #присоединяем к тому что легло на стол
  deck.remove(a)           #и удаляем из колоды
#И выводим их на экран 
print('Разданные карты:')
for card in hand:
  print (card.short_name, end = ' ')
#Рассчитываем вероятность выпадения оставшихся в колоде карт
probability = round ((1 / len(deck)) * 100, 2)
#Выводим информацию о том что осталось в колоде
print('\n')
print('Оставшиеся карты в колоде:')
for card in deck:
  print(card.short_name)
print(f'Вероятность вытащить одну из этих карт: {probability}%')