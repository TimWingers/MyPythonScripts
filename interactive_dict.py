dict = {}
print('Hi, user. What do you want?')
while True:
  x1 = input('Add or find words? (add/find/exit) ')  
  if x1 == 'add':
    key = input('Enter a word: ')
    value = input('Enter a definition: ')
    dict[key] = value
    print('The word is added to dict!')
    print(dict)
  elif x1 == 'find':
    fnd = input('Enter a word: ')
    if fnd in dict:
      print(dict[fnd])
    else:
      print('This word is not exist!')
  elif x1 == 'exit':
    break