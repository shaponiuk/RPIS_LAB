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

bDaysPre = [
  0 for x in range(0, 12 * 31 + 1)
]

i = 0;

for month in bDays:
  for day in month:
    i += 1
    bDaysPre[i] = bDaysPre[i - 1] + day




















