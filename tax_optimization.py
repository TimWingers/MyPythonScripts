#Поиск лучшей налоговой ставки
import matplotlib.pyplot as plt
import math
def revenue(tax):
  return(100 * (math.log(tax + 1) - (tax - 0.2)**2 + 0.04))

xs = [x/1000 for x in range(1001)]
ys = [revenue(x) for x in xs]
plt.plot(xs,ys)
current_rate = 0.6
plt.plot(current_rate,revenue(current_rate),'ro')
plt.title('Tax Rates and Revenue')
plt.xlabel('Tax Rate')
plt.ylabel('Revenue')
plt.show()

def revenue_derivative(tax):
  return(100 * (1/(tax + 1) - 2 * (tax - 0.2)))

#Градиентный подъем
threshold = 0.0001
maximum_iterations = 100000
keep_going = True
iterations = 0
step_size = 0.01

while(keep_going):
  rate_change = step_size * revenue_derivative(current_rate)
  current_rate = current_rate + rate_change
  
  if(abs(rate_change) < threshold):
    keep_going = False

  if(iterations >= maximum_iterations):
    keep_going = False

  iterations = iterations+1