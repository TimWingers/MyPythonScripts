import numpy as np
import matplotlib.pyplot as plt

points = np.arange(-5, 5, 0.01) #строит матрицу с 1000 равноудаленных точек
xs, ys = np.meshgrid(points, points)

z = np.sqrt(xs ** 2 + ys ** 2)
z   #получаем координаты рассеивания

plt.imshow(z, cmap=plt.cm.gray)
plt.title('Image plot of $\sqrt{x^2 + y^2}$ for a grid of values')
plt.colorbar  #выводит график