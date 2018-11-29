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
bDaysMax = 0

for month in bDays:
  for b in month:
    bDaysSum += b
    if b > bDaysMax:
      bDaysMax = b

bDaysPre = [
  0 for x in range(0, 12 * 31 + 1)
]

bDaysNum = [
  0 for x in range(0, 12 * 31)
]

i = 0;

for month in bDays:
  for day in month:
    bDaysNum[i] = day
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
bDayFProbs = [
  bDaysNum[x] / bDaysMax for x in range(0, len(bDaysNum))
]
bDayFProbsAr = np.array(bDayFProbs)

def randDay2AA(n):
  x = np.random.randint(0, len(birthDayProbs))
  p = np.random.random()

  while p > bDayFProbsAr[x]:
    x = np.random.randint(0, len(birthDayProbs))
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

def findRep2A(a):
  x = [0 for x in range(0, len(bDaysPre) - 1)]
  randomDay = randDay2AA(0)
  counter = 0

  while(x[randomDay - 1] == 0):
    x[randomDay - 1] = 1
    randomDay = randDay2AA(0)
    counter += 1

  return counter

#bParList2A = [
#  findRep2A(0)
#    for x in range(0, 10000)
#]

#plt.hist(bParList2A, density = 1)
#plt.show()

#print(np.average(bParList2A))
#print(st.mode(bParList2A))
#print(np.median(bParList2A))

nOfBDays = len(bDayProbsAr)

def randDay2B(n):
  randomDays = np.random.randint(0, nOfBDays, n)
  randomProbs = np.random.uniform(0, 1, n)
  randomDayFProbs = bDayFProbsAr[randomDays] 
  result = randomProbs <= randomDayFProbs

  falseIndexes = []

  for x in range(0, n):
    if not result[x]:
      falseIndexes.append(x)
  
  if len(falseIndexes) > 0:
    randomDays[falseIndexes] = randDay2B(len(falseIndexes)) 

  return randomDays

def findRep2B(n):
  randomDays = randDay2B(2 * n)
  counters = []
  rdIndex = 0

  for i in range(0, n):
    counter = 0
    s = set()

    while randomDays[rdIndex] not in s:
      s.add(randomDays[rdIndex])
      counter += 1
      rdIndex += 1

      if rdIndex == 2 * n:
        rdIndex = 0
        randomDays = randDay2B(2 * n)

    counters.append(counter)
    
  return counters

bParList2B = findRep2B(1000)

#print(np.mean(bParList2B))
#print(st.mode(bParList2B))
#print(np.median(bParList2B))

n = len(bDayProbsAr)

buckets = [
  [(i, bDayProbsAr[i])] for i in range(n)
  #[(0, 0.2)], [(1, 0.25)], [(2, 0.3)], [(3, 0.15)], [(4, 0.1)]
]

n = len(buckets)
V = round(1 / n, 19)

def getCont(i):
  s = 0

  for x in buckets[i]:
    s += x[1];

  return s

def transferProbability(fromB, toB):
  #print("transferProbability", fromB, toB)
  st = getCont(toB)

  while st < V and len(buckets[fromB]) > 0:
    fTup = buckets[fromB][len(buckets[fromB]) - 1]
    #print(fTup)

    diff = round(V - st, 20)
    #print(diff)

    if fTup[1] > diff:
      tup = (fTup[0], diff)
      buckets[toB].append(tup);
      buckets[fromB][len(buckets[fromB]) - 1] = (fTup[0], round(fTup[1] - diff, 20))
      break
    else:
      buckets[toB].append(buckets[fromB][len(buckets[fromB]) - 1])
      buckets[fromB].pop()
      st = getCont(toB)

def checkBucketsLoop():
  for i in range(n):
    si = getCont(i)

    if si < V:
      #print("i", i, si)

      for j in range(n):
        if j == i:
          continue
        else:
          sj = getCont(j)
            
          if sj > V:
            #print("j", j, sj)
            transferProbability(j, i)
            return True

  return False



def checkBuckets():
  while checkBucketsLoop():
    ()
            
checkBuckets()

print(buckets)

for x in range(n):
  print(getCont(x))











