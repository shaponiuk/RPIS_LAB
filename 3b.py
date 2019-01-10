import matplotlib.pyplot as plt
import numpy as np
import math

def abs(a):
  if a < 0:
    return -1 * a
  else:
    return a

def f(k):
  if k == 0.0:
    return 1.0 / 2.0
  else:
    return 1.0 / (4.0 * abs(k) * (abs(k) + 1.0))

indexes = [
  i for i in range(-10, 11)
]

values = [
  f(k) for k in indexes
]

#plt.plot(values)
#plt.show()

def get_x(y):
  delta = 1.0 + 1.0 / y
  delta_sqrt = math.sqrt(delta)

  return (-1.0 + delta_sqrt) / 2.0

def rand_sign():
  r = np.random.random()

  if r < 0.5:
    return -1
  else:
    return 1

def sample():
  y = np.random.random()

  if y > 0.5:
    return sample()

  if y == 0.5:
    return 0;

  x = get_x(y)

  return rand_sign() * int(round(x))

N = 10000

samples = [
  sample() for i in range(N)
]

def pseudo_mean(i):
  sum = 0

  for a in range(i):
    sum += samples[a]

  return float(sum) / float(i)

pseudo_means = [
  pseudo_mean(i + 1) for i in range(N)
]

#plt.plot(pseudo_means)
#plt.show()

def median(i):
  l = [ samples[a] for a in range(i) ]
  m = np.median(l)
  return m

medians = [
  median(i + 1) for i in range(N)
]

#plt.plot(medians)
#plt.show()
