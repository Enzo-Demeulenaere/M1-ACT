import random
import time

def read_file_and_extract_values(filename):
    l = []
    with open(filename, 'r') as file:
        n = int(file.readline())
        for line in file:
            values = list(map(int, line.split()))
            l.append([values[0],values[1],values[2]])
    return n, l

def calcul_ordonnancement(l):
    t = 0
    time_task_end = []
    for i in range(len(l)):
        t += l[i][0]
        time_task_end.append(l[i][1] * max(t-l[i][2],0))
    score_ordonnancement = sum(time_task_end)
    return score_ordonnancement
    
def ordonnancement_aleatoire(l):
    return random.shuffle(l)

def heuristique_constructive_poids_diviser_time_execution(l):
    l = sorted(l, key=lambda x: x[1] / x[0], reverse=True)
    return calcul_ordonnancement(l)

def generer_paires_index(l, indice):     #fonction utilitaire
    paires = [[indice, j] for j in range(indice + 1, len(l))]
    return paires

def generer_toutes_permutations(n):      #fonction utilitaire
    return [[i, j] for i in range(1, n+1) for j in range(i+1, n+1)]

def swap_amelioration_temps(l, swap, temps):
    t = temps
    for j in range (len(swap)):
        a, b = swap[j][0], swap[j][1]
        z0, z1 = l[a], l[b]
        l[a], l[b] = z1, z0
        calcul = calcul_ordonnancement(l)
        if calcul < t:
            t = calcul
            i0, i1 = a, b
        l[a], l[b] = z0, z1
    if t < temps:
        z0, z1 = l[i0], l[i1]
        l[i0], l[i1] = z1, z0
        return l, t, True 
    else:
        return l, temps, False 
    
def heuristique_hill_climbing_voisinage_swap(l):
    temps = calcul_ordonnancement(l)
    i = 0
    while i < len(l):
        swap = generer_paires_index(l,i)
        l, temps, boo = swap_amelioration_temps(l, swap, temps)
        if boo == False:
            i += 1
        else:
            i == 0
    return calcul_ordonnancement(l), l              

def perturbationSwap(liste,nbSwap):
    n = len(liste)
    for i in range(nbSwap):
        i1 = 0
        i2 = 0
        while (i1 == i2):
            i1 = random.randint(0,n-1)
            i2 = random.randint(0,n-1)
        liste[i2], liste[i1] = liste[i1], liste[i2]
    return liste

def ils_repetition_sans_meilleure_perturbation_avec_n_swap(liste,repetition,n):
    start = time.time()
    s = f(liste)
    sEtoile,listeSolution = heuristique_hill_climbing_voisinage_swap(liste)
    nbPerturbation = 0
    while (nbPerturbation < repetition):
        listePerturbation = perturbationSwap(listeSolution,n)
        sPrime = f(listePerturbation)
        sEtoilePrime, listeSolutionPrime = heuristique_hill_climbing_voisinage_swap(listePerturbation)
        sEtoile = min(sEtoile,sEtoilePrime)
        if (sEtoile != sEtoilePrime): # si la perturbation n'est pas meilleure
            nbPerturbation +=1
        else:
            nbPerturbation=0
            listeSolution = listeSolutionPrime
    end = time.time()
    timeSpent = end - start
    return sEtoile , timeSpent

def f(liste):
    return calcul_ordonnancement(liste)

""" filename = "SMTWP/n1000_2_b.txt"
n, l = read_file_and_extract_values(filename) """
""" print("n:", n)
print("l:", l)
print("\n")
s = calcul_ordonnancement(l)
print("Le score d'ordonnancement est : " + str(s))
print("\n")
hc = heuristique_hill_climbing_voisinage_swap([[1,2,6],[1,3,7],[3,1,10],[2,5,4],[3,3,8]])
print("Le score de l'heuristique hill climbing swap est : " + str(hc))
print("\n") """

""" files = [15,16,17,18,19,35,36,37,38,39,40,41,42,43,44,85,86,87,88,89]
optimaux = [172995,407703,332804,544838,477684,19114,108293,181850,90440,151701,129728,462324,425875,320537,360193,284,66850,84229,55544,54612]
resPourcentages = []
resTemps = []
for i in range(len(files)):
    fileNumber = files[i]
    filename = f"SMTWP/n100_{fileNumber}_b.txt"
    n,l = read_file_and_extract_values(filename)
    res,temps = ils_repetition_sans_meilleure_perturbation_avec_n_swap(l,5,10)
    resPourcentages.append((res-optimaux[i])/optimaux[i])
    resTemps.append(temps)
resMoy = sum(resPourcentages)/len(resPourcentages)
tempsMoy = sum(resTemps)/len(resTemps)

print("pourcentage moyen : ",resMoy)
print("temps moyen: ",tempsMoy) """

""" print("Ils sur "+filename) 
print(ils_repetition_sans_meilleure_perturbation_avec_n_swap(l,5,10))
print("====") """

""" 5pourcentages qui sont la moyenne des pourcentage de tous,
moyenne des pourcentages,
indiquer les parametres
"""

pourcentages = [0.03144934878993798,0.046555790930817166,0.03000254648270053,0.05359722893511476,0.05397776904676872]
temps = [2.360936141014099,2.2349747896194456,2.3522191882133483,2.1312528014183045,2.377146327495575]

print(sum(pourcentages)/5)
print(sum(temps)/5)
