import copy
import sys

f = open(sys.argv[1],"r")      #moyen de lire les fichiers tests
n = int(f.readline())
m = int(f.readline())

echiquier = []
for i in range(n):
    line = f.readline()
    newline=[]
    for j in range(m):
        if line[j] == "p":
            newline.append(2)
        elif line[j] == 'P':
            newline.append(1)
        else:
            newline.append(0)
    echiquier.append(newline)

""" echiquier = [
    [2,2,2,2],
    [0,0,0,0],
    [1,1,1,1]
    ]

n = 3
m = 4 """

tour=0
dico = {} # clé : str(tour%2,plateau) => valeur : configuration()

def configuration (l):
    #print("liste")
    #print(l)
    if sum([abs(x) for x in l]) > sum(l):
        config = -(max([x for x in l if x<0])+1)
    else:
        config = -(max(l)+1)
    #print("resultat")
    #print(config)
    return config
        
def plusDeCoup (plateau,tour):
    idCouleur = tour%2 +1 #blancs vaudront 1 
    idAdversaire = idCouleur%2 + 1 #noirs vaudront 2
    #case vide vaudra 0  

    equipe = [] 
    for i in range(n):
        for j in range(m):
            if plateau[i][j]==idCouleur:
                equipe.append([i,j])

    for pion in equipe:
        x = pion[1]
        y = pion[0]
        nexty = y
        if idCouleur == 1:  
            nexty = y-1
        else :
            nexty = y+1
        #diagonale gauche
        if x>0 and plateau[nexty][x-1]==idAdversaire:        
            return False
        #cas diagonale droite
        if x<m-1 and plateau[nexty][x+1]==idAdversaire:
            return False
        #cas vide devant
        if plateau[nexty][x]==0:
            return False
    return True

def tostr(plateau,tour):
    res = str(tour)
    for ligne in plateau:
        for i in ligne:
            res+=str(i)
    return res

def evaluation (plateau,l,h,tour):
    #print("start")
    #print(plateau,l,h,tour)
    tmpcle = tostr(plateau,tour%2)
    for cle, valeur in dico.items():
        if cle == tmpcle:
            print("-----JAI TROUVE------")
            return valeur
    
    if [x for x in plateau[l-1] if x==2] != []:
        dico[tostr(plateau,tour%2)]=(tour-1)
        #print("ADD TO DICO",dico) 
        return (tour-1)
    elif [x for x in plateau[0] if x==1] != []:
        dico[tostr(plateau,tour%2)]=-(tour+1)
        #print("ADD TO DICO",dico)
        return -(tour+1)
    elif plusDeCoup (plateau,tour):
        if tour%2 == 0:
            dico[tostr(plateau,tour%2)]=(tour-1)
            #print("ADD TO DICO",dico)
            return (tour-1)
        else:
            dico[tostr(plateau,tour%2)]=-(tour+1)
            #print("ADD TO DICO",dico)
            return -(tour+1)
    else:
        s = successeurs(plateau,l,h,tour)
        e = []
        #print("successeurs : ")
        #print(s)
        for i in s:
            #print("success")
            e.append(evaluation(i,l,h,tour+1))
    memoire = configuration(e)
    dico[tostr(plateau,tour%2)]=memoire
    #print("ADD TO DICO",dico)
    return memoire
    
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

        #il faut encore flatten la liste
    return sum(res, [])

res =evaluation(echiquier,n,m,tour)
print("---RESULTAT FINAL---")
print(res)

#resultats des fichiers tests
#3x4_1 => 1
#3x4_-2 => -2
#4x4_0 => 0  
#4x4_11 => 11  
#5x5_1 => 1
#5x5_3 => 3
#5x5_15 => 13     X
#5x5_-2 => -2
#5x5_n-2 => 1     X (normal)
#5x5_19 => 19
#6x6_3 => 3
#6x6_5 => 5
#6x6_x => too long
