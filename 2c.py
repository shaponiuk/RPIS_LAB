import csv
import numpy as np

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

bDaysNum = [0 for x in range(0, 12 * 31)]

i = 0

for month in bDays:
  for day in month:
    bDaysNum[i] = day
    i += 1

bDaysNumAr = np.zeros(12 * 31)

i = 0

for b in bDaysNum:
  bDaysNumAr[i] = b
  i += 1

n = len(bDaysNumAr)
v = round(1 / n, 22)

buckets = [
  [(i + 1, bDaysNumAr[i] / bDaysSum)] for i in range(n)
]

def getCont(i):
  s = 0

  for x in buckets[i]:
    s += x[1]

  return s

def transferProbability(fromB, toB):
  st = getCont(toB)

  while st < v and len(buckets[fromB]) > 0:
    fromBLastI = len(buckets[fromB]) - 1
    # buckets[fromB] has only one element
    # we can take it blindly
    fTup = buckets[fromB][fromBLastI]
    diff = round(v - st, 22)
    
    if fTup[1] > diff:
      tup = (fTup[0], diff)
      buckets[toB].append(tup)
      buckets[fromB][fromBLastI] = (fTup[0], round(fTup[1] - diff, 22))
      break
    else:
      buckets[toB].append(buckets[fromB][fromBLastI])
      buckets[fromB].pop()
      st = getCont(toB)

def checkBucketsLoop():
  for i in range(n):
    si = getCont(i)

    if si < v:
      for j in range(n):
        if j == i:
          continue
       
        sj = getCont(j)
        
        if sj > v:
          transferProbability(j, i)
          return True

  return False

def squareBuckets():
  while checkBucketsLoop(): ()

squareBuckets()

bucketsAr = np.array(buckets)

def sampleVec(count):
  bucketIndexes = np.random.random_integers(0, high = n - 1, size = count)
  placesInBucket = np.random.rand(count)
  chosenBuckets = bucketsAr[bucketIndexes]
  returnArray = np.empty([count])

  i = 0

  for bucket in chosenBuckets:
    placesInBucket[i] *= getCont(bucketIndexes[i])
    s = 0
    j = 0
    
    for x in bucket:
      s += x[1]
      
      if placesInBucket[i] < s:
        returnArray[i] = x[0]
        break

      j += 1

    i += 1

  return returnArray

print(sampleVec(1000000))










