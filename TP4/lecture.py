import copy
import sys
import time

f = open(sys.argv[1],"r")      #moyen de lire les fichiers tests
n = int(f.readline())

temps = []
poids = []
date = []

for i in range(n):
    values = f.readline().split()
    temps.append(int(values[0]))
    poids.append(int(values[1]))
    date.append(int(values[2]))

print(temps)
print("\n=============================================\n")
print(poids)
print("\n=============================================\n")    
print(date)