import numpy as np
import matplotlib.pyplot as plt
import plotly as py
import plotly.graph_objs as go
import math

lam = 10
x = np.random.poisson(lam, 1000)

#plt.hist(x, bins = 21);
#plt.show()

std_dev = np.std(x)

print(std_dev)

pre_sums = [0 for x in range(1000)]

for i in range(1000):
  if i == 0:
    pre_sums[i] = x[i]
  else:
    pre_sums[i] = pre_sums[i - 1] + x[i]

avgs = [ 
  pre_sums[i] / (i + 1) for i in range(1000) 
]

def square(n):
  return n * n

expected_value = lam

lambdas = [ lam for i in range(1000) ]

std_devs = [
  math.sqrt(lam / (i + 1)) for i in range(1000)
]

l_plus_s = [
  lam + std_devs[i] for i in range(1000)
]

l_minus_s = [
  lam - std_devs[i] for i in range(1000)
]

plt.plot(avgs)
plt.plot(lambdas)
plt.plot(l_plus_s)
plt.plot(l_minus_s)
plt.show()
