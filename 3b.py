import matplotlib.pyplot as plt
import numpy as np
import math

def abs(a):
  if a < 0:
    return -1 * a
  else:
    return a

def f(k):
  if k == 0:
    return 1.0 / 2.0
  else:
    return 1.0 / (4.0 * abs(k) * (abs(k) + 1.0))

indexes = [
  i for i in range(-10, 11)
]

values = [
  f(k) for k in indexes
]

plt.plot(values)
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

print(sample())
