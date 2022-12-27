#Возведение в степень с помощью функции
def myPow(x,n):
  sx = 1
  while n > 0:
    sx *= x
    n -= 1
  return sx
p = myPow (3, 5)
print(p)