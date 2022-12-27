import random
import string
adjectives = ['sleepy', 'slow', 'hot', 'cold', 'big', 'red', 'orange', 'yellow', 'green', 'blue', 'gold', 'old', 'white', 'free', 'spicy', 'brave']
nouns = ['apple', 'dinosaur', 'ball', 'cat', 'goat', 'dragon', 'car', 'duck', 'panda', 'telephone', 'banana', 'teacher']
print('Welcome! Choose your new password: ')

while True:
  for num in range(3):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0,100)
    special_char = random.choice(string.punctuation)
    password1 = adjective + noun + str(number) + special_char
    password2 = noun + special_char + adjective + str(number) 
    password3 = special_char + noun + str(number) + adjective
    print(password1)
    print(password2)
    print(password3)

  response = input('Do you want to generate more passwords? (y/n) ')
  if response == 'n':
    break