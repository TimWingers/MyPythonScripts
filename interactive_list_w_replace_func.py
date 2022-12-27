names = []
x1 = input('Write a 1st name ')
names.append(x1)
x2 = input('Write a 2nd name ')
names.append(x2)
x3 = input('Write a 3rd name ')
names.append(x3)
x4 = input('Write a 4th name ')
names.append(x4)
x5 = input('Write a 5th name ')
names.append(x5)
print(names)

x6 = input('Is it correct? What name needs to be replaced? ')
if x6 in names:
  y = names.index(x6)
  x7 = input('What is a correct name? ')
  names[y] = x7
  print(names)
else:
  print('Error! There are no such name in the list')