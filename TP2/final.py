import copy
import sys
import time

f = open(sys.argv[1],"r")      #moyen de lire les fichiers tests
l = int(f.readline())
h = int(f.readline())

echiquier = []
for i in range(l):
    line = f.readline()
    newline=[]
    for j in range(h):
        if line[j] == "p":
            newline.append(2)
        elif line[j] == 'P':
            newline.append(1)
        else:
            newline.append(0)
    echiquier.append(newline)

""" plateau = [
 [2,2,2,2],   
 [0,0,0,0],
 [0,0,0,0],
 [1,1,1,1]
 ]

l = 4
h = 3  """

tour=0

def configuration (l):
    if any(element == 0 for element in l):
        config = 1
    elif sum([abs(x) for x in l]) > sum(l):
        config = (min([abs(x) for x in l if x<0])+1)
    else:
        config = -(max(l)+1) 
    return config

""" def plusDeCoup (plateau,l,h,tour):
    idCouleur = tour%2 +1 #blancs vaudront 1 
    idAdversaire = idCouleur%2 + 1 #noirs vaudront 2
    #case vide vaudra 0  
 
    for i in range(l):
        for j in range(h):
            if plateau[i][j]==idCouleur:
                nexti = i
                if idCouleur == 1:  
                    nexti = i-1
                else :
                    nexti = i+1
                #cas vide devant
                if plateau[nexti][j]==0:
                    return False
                #diagonale gauche
                if j>0 and plateau[nexti][j-1]==idAdversaire:        
                    return False
                #cas diagonale droite
                if j<h-1 and plateau[nexti][j+1]==idAdversaire:
                    return False
    return True """

def plusDeCoup (plateau,l,h,tour):
    if tour%2 == 0:
        for i in range (1,l):
            for j in range (h):
                if plateau[i][j] == 1:
                    if plateau [i-1][j] == 0:
                        return False
                    if j!=0 and j!=h-1 and (plateau[i-1][j-1] == 2 or plateau[i-1][j+1] == 2):
                        return False
                    if j==0 and plateau[i-1][j+1] == 2:
                        return False
                    if j==h-1 and plateau[i-1][j-1] == 2:
                        return False
    if tour%2 == 1:
        for i in range (l-1):
            for j in range (h):
                if plateau[i][j] == 2:
                    if plateau [i+1][j] == 0:
                        return False
                    if j!=0 and j!=h-1 and (plateau[i+1][j-1] == 1 or plateau[i+1][j+1] == 1):
                        return False
                    if j==0 and plateau[i+1][j+1] == 1:
                        return False
                    if j==h-1 and plateau[i+1][j-1] == 1:
                        return False
    return True

def evaluation_dynamique(plateau,l,h,tour):
    memoization_table = {}
    return evaluation(memoization_table,plateau,l,h,tour)

def evaluation(memoization_table,plateau,l,h,tour):
    plateau_str = str(plateau)
    if plateau_str in memoization_table:
        return memoization_table[plateau_str]
    
    if [x for x in plateau[len(plateau)-1] if x==2] != []: 
        return 0
    elif [x for x in plateau[0] if x==1] != []:
        return 0
    elif plusDeCoup (plateau,l,h,tour):
        return 0
    else:
        s = successeurs(plateau,l,h,tour)
        e = []
        for i in s:
            e.append(evaluation(memoization_table,i,l,h,tour+1))
        result = configuration(e)
    memoization_table[plateau_str] = result
    return result

def evaluation_naive(plateau,l,h,tour):
    if [x for x in plateau[len(plateau)-1] if x==2] != []: 
        return 0
    elif [x for x in plateau[0] if x==1] != []:
        return 0
    elif plusDeCoup (plateau,l,h,tour):
        return 0
    else:
        s = successeurs(plateau,l,h,tour)
        e = []
        for i in s:
            e.append(evaluation_naive(i,l,h,tour+1))
    return configuration(e)

def successeurs(echiquier,n,m,tour):

    idCouleur = tour%2 +1 #blancs vaudront 1 
    idAdversaire = idCouleur%2 + 1 #noirs vaudront 2
    #case vide vaudra 0  

    equipe = [] 
    for i in range(n):
        for j in range(m):
            if echiquier[i][j]==idCouleur:
                equipe.append([i,j])  

    res = []
    for pion in equipe:
        x = pion[1]
        y = pion[0]
        nexty = y
        if idCouleur == 1:  
            nexty = y-1
        else :
            nexty = y+1
        suivants = [] 
        #diagonale gauche
        if x>0 and echiquier[nexty][x-1]==idAdversaire:        
            newCopy = copy.deepcopy(echiquier)
            newCopy[y][x]=0
            newCopy[nexty][x-1]=idCouleur
            suivants.append(newCopy)

        #cas diagonale droite
        if x<m-1 and echiquier[nexty][x+1]==idAdversaire:
            newCopy = copy.deepcopy(echiquier)
            newCopy[y][x]=0
            newCopy[nexty][x+1]=idCouleur
            suivants.append(newCopy)

        #cas vide devant
        if echiquier[nexty][x]==0:
            newCopy = copy.deepcopy(echiquier) 
            newCopy[y][x]=0
            newCopy[nexty][x]=idCouleur
            suivants.append(newCopy)
        # on ajoute toutes les copies à la res list
        res.append(suivants)
    return sum(res, [])

nombre_repets = 1
temps_total_vDynamique = 0
for _ in range(nombre_repets):
    debut = time.time()
    print(evaluation_dynamique(echiquier,l,h,tour))
    fin = time.time()
    temps_total_vDynamique += fin - debut

temps_moyen_vDynamique = temps_total_vDynamique / nombre_repets
print("Temps moyen de vDynamique : "+str(temps_moyen_vDynamique))

""" temps_total_vNaive = 0
for _ in range(nombre_repets):
    debut = time.time()
    print(evaluation_naive(echiquier,l,h,tour))
    fin = time.time()
    temps_total_vNaive += fin - debut

temps_moyen_vNaive = temps_total_vNaive / nombre_repets
print("Temps moyen de vNaive : "+str(temps_moyen_vNaive)) """