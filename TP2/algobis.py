import copy

echiquier = [
    [0,2,0,2],
    [2,1,0,0],
    [0,0,1,1]
    ]

n = 3
m = 4

tour=0
def successeurs(echiquier,n,m,tour):

    idCouleur = tour%2 +1 #blancs vaudront 1 
    idAdversaire = idCouleur + 1 #noirs vaudront 2
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


suc = successeurs(echiquier,n,m,tour)

for each in suc :
    for a in each:
        print(a)
    print("----------")