import sys
import random

trigrams = []

#http://home.ccil.org/~cowan/trigrams
f = open('trigrams.txt')

for line in f:
    row = line.split('\t')
    row[0] = row[0].replace("#", " ").lower()
    trigrams.extend([row[0]]*int(float(row[1])))
idx = len(trigrams)
while True:
    sys.stdout.write(trigrams[random.randint(0, idx-1)])
    sys.stdout.flush()
