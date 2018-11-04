import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

bDays = [
  [
    0 for x in range(1, 32)
  ] for y in range(1, 13)
]

with open('us_births_69_88.csv') as csvfile:
  reader = csv.DictReader(csvfile)

  for row in reader:
    m = int(row['month'])
    d = int(row['day'])
    b = int(row['births'])
    bDays[m - 1][d - 1] = b

bDaysSum = 0

for month in bDays:
  for b in month:
    bDaysSum += b

bDaysPre = [
  0 for x in range(0, 12 * 31 + 1)
]

i = 0;

for month in bDays:
  for day in month:
    i += 1
    bDaysPre[i] = bDaysPre[i - 1] + day

def randNum():
  return np.random.randint(0, bDaysSum)

def randDay1C():
  x = randNum()

  a = 0
  b = len(bDaysPre) - 1
  m = (a + b) // 2

  while a < b and m > 0:
    if bDaysPre[m] < x:
      a = m + 1
      m = (a + b) // 2
    elif bDaysPre[m - 1] >= x:
      b = m - 1
      m = (a + b) // 2
    else:
      a = b

  return m

birthDayProbs = []

for month in bDays:
  for b in month:
    birthDayProbs.append(b / bDaysSum)

bDayProbsAr = np.array(birthDayProbs)

def randDay2AA():
  x = np.random.randint(0, len(bDayProbs))
  p = np.random.random()

  while p > bDayProbs[x]:
    x = np.random.randint(0, len(bDayProbs))
    p = np.random.random()

  return x + 1

#The random day(x) is between 1 and len(bDayProbs)
#The choices of x and p are independent
#random p gives us the correct probability for the bDayProbs distribution
#p will sometime have value equal to 0.0, the algorithm will end at that point
#(or earlier)

def randDay2A(x):
  return np.random.choice(
    np.arange(1, len(bDayProbsAr) + 1), p = bDayProbsAr
  )

def findRep2A():
  x = [0 for x in range(0, len(bDaysPre) - 1)]
  randomDay = randDay2A(0)
  counter = 0

  while(x[randomDay - 1] == 0):
    x[randomDay - 1] = 1
    randomDay = randDay2A(0)
    counter += 1

  return counter

#bParList2A = [
#  findRep2A()
#    for x in range(0, 1000)
#]

#plt.hist(bParList2A, density = 1)
#plt.show()

#print(np.average(bParList2A))
#print(st.mode(bParList2A))
#print(np.median(bParList2A))

randDay2BVec = np.vectorize(randDay2A) 

def findRep2B():
  x = set()
  zAr = np.zeros(len(bDayProbsAr) + 1)
  randomDays = randDay2BVec(zAr)
  counter = 0

  while randomDays[counter] not in x:
    x.add(randomDays[counter])
    counter += 1
    
  return counter

bParList2B = [
  findRep2B()
    for x in range(0, 1000)
]

print(np.mean(bParList2B))
print(st.mode(bParList2B))
print(np.median(bParList2B))





















