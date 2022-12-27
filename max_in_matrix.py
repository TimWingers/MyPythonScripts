def max(l):
  max = 0
  r = 0

  for i in range(len(l)):
    for j in range(len(l[0])):
      if l[i][j] > max:
        max = l[i][j]

  for i in range(len(l)):
    for j in range(len(l[0])):
      if l[i][j] == max:
        r = '(' + str(i+1) + ';' + str(j+1) + ')'
        print('Максимальный элемент: ', max)
        return r

n = int(input('Количество строк матрицы: '))
m = int(input('Количество столбцов матрицы: '))
h = []

for i in range(n):
  h.append([])
  c = input()
  h[i] = c.split(' ')

for i in range(n):
  for j in range(m):
    h[i][j] = int(h[i][j])

print(max(h))

#Количество строк матрицы: 3
#Количество столбцов матрицы: 5
#41 34 36 38 35
#42 39 43 40 35
#32 44 39 41 43
#Максимальный элемент:  44
#(3;2)