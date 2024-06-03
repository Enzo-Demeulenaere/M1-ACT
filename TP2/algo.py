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
    if tour%2 == 0 : #tour des blancs
        blancs = []
        for i in range(n):
            for j in range(m):
                if echiquier[i][j]==1 :
                    blancs.append([i,j])
        # on a la liste des pions blancs
        res = []
        for pion in blancs :
            x = pion[1]
            y = pion[0]
            suivants = []
            #cas diagonale gauche
            if x>0 and echiquier[y-1][x-1]==2:        
                newCopy = copy.deepcopy(echiquier)
                newCopy[y][x]=0
                newCopy[y-1][x-1]=1
                suivants.append(newCopy)

            #cas diagonale droite
            if x<m-1 and echiquier[y-1][x+1]==2:
                newCopy = copy.deepcopy(echiquier)
                newCopy[y][x]=0
                newCopy[y-1][x+1]=1
                suivants.append(newCopy)

            #cas vide devant
            if echiquier[y-1][x]==0:
                newCopy = copy.deepcopy(echiquier) 
                newCopy[y][x]=0
                newCopy[y-1][x]=1
                suivants.append(newCopy)
            # on ajoute toutes les copies à la res list
            res.append(suivants)
        
        #il faut encore flatten la liste
        return sum(res, [])


    else : # tour des noirs
        noirs = []
        for i in range(n):
            for j in range(m):
                if echiquier[i][j]==2 :
                    noirs.append([i,j]) 
        # on a la liste des pions noirs
        res = []
        for pion in noirs:
            x = pion[1]
            y = pion[0]
            suivants = []
            #cas diagonale gauche
            if x>0 and echiquier[y+1][x-1]==1:        
                newCopy = copy.deepcopy(echiquier)
                newCopy[y][x]=0
                newCopy[y+1][x-1]=2
                suivants.append(newCopy)

            #cas diagonale droite
            if x <m-1 and echiquier[y+1][x+1]==1:
                newCopy = copy.deepcopy(echiquier)
                newCopy[y][x]=0
                newCopy[y+1][x+1]=2
                suivants.append(newCopy)

            #cas vide devant
            if echiquier[y+1][x]==0:
                newCopy = copy.deepcopy(echiquier)
                newCopy[y][x]=0
                newCopy[y+1][x]=2
                suivants.append(newCopy)
            # on ajoute toutes les copies à la res list

            res.append(suivants)
        
        #il faut encore flatten la liste
        return sum(res, [])

suc = successeurs(echiquier,n,m,tour)

for each in suc :
    print(each)
    print("----------")