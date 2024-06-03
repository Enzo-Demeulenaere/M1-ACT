import copy
import sys
import time




f = open(sys.argv[1],"r")      #moyen de lire les fichiers tests
n = int(f.readline())

temps = []
poids = []
date = []

c = [0] * (n+1)
res = (n+1)*[0]
l = []

for i in range(n):
    values = f.readline().split()
    temps.append(int(values[0]))
    poids.append(int(values[1]))
    date.append(int(values[2]))
    l.append(i+1)

def ordonnancement_aleatoire(l1,l2,l3):
    l = []
    for i in range (len(l1)):
        zzz = [l1[i],l2[i],l3[i]]
        l.append(zzz)
    random.shuffle(l)
    a = []
    b = []
    c = []
    for i in range (len(l)):
        a.append(l[i][0])
        b.append(l[i][1])
        c.append(l[i][2])
    return a, b, c


def f(liste):
    print(liste)
    time = 0
    for tache in liste:
        time += temps[tache-1]
        c[tache]=time
        retard=max(time-date[tache-1],0)
        res[tache]=poids[tache-1]*retard
    return sum(res)

# Heuristique : trier les taches par date d'expiration croissante

def ordonnancement_expiration_croissante(temps,poids,date):
    l =[]
    for i in range (len(temps)):
        t = [i+1,poids[i],date[i]]
        l.append(t)
    l = sorted(l, key = lambda x: x[1]/x[2] ,reverse = True)
    res = []
    for i in range (len(l)):
        res.append(l[i][0])
    return res


print(f(ordonnancement_expiration_croissante(temps,poids,date)))        