# Rapport ACT TP1 | Diviser pour régner

## Q1

* Une première approche peut être basée sur la remarque suivante : un rectangle de surface maximale res-
pectant les contraintes a nécessairement deux sommets de la forme (xi , 0), (xj , 0) avec 0 ≤ i < j ≤ n − 1
(Pourquoi ?).

Cette remarque s'explique par le fait que les rectangles ont pour contrainte d'avoir une base sur l'axe des x, cette face aura naturellement 2 points avec des coordonnées de la forme (xi,0), (xj,0) avec 0 ≤ i < j ≤ n − 1

* Comment exprimer la surface du rectangle de surface maximale respectant les contraintes et dont deux
sommets sont (xi , 0), (xj , 0) ?

La surface sera trivialement exprimée par un calcul d'aire - longueur * largeur - où la longueur sera le résultat de xj - xi, la largeur l implique le fait que notre rectangle aura pour sommets les points : (xi,0), (xi,l), (xj,l), (xj,0). 

- Remarque: l correspondra à la borne de l'axe y ou à la coordonnée y d'un des points présents dans la surface de travail

Pour l'algorithme avec une compléxité en ø(n²), l'objectif est de parcourir dans une première boucle i tout les points, puis dans une seconde boucle imbriquée j, on parcours le reste des points en faisant attention à retenir la hauteur de points la plus petite parcourue minH, on calculera ensuite la surface du rectangle avec xj-xi comme longueur et minH parcourue. Au préalable nous ajouterons à notre liste de points les points (0,0) et (l,h) afin de s'assurer de commencer à l'origine et de terminer avec le coin supérieur droit.

- Remarque : minH vaut la hauteur maximale h par défaut lorsque i et j sont deux points consécutifs

Notre algorithme est donc le suivant : 

```python
def algo_n2(l,h,points):
    print(points)
    bestRect=0
    for i in range(n):
        pointI = points[i]
        minH = h
        for j in range (i+1,n):
            if j> i+1 :
                minH = min(minH, points[j-1][1])
            pointJ = points[j]
            longueur = pointJ[0]-pointI[0]
            rect = longueur * minH
            bestRect = max(bestRect,rect)
    return bestRect
```  

Cet algorithme a été testé sur les "petits" jeux de données (entre 0 et 500 points) et s'avère correct (exception faite pour le fichier 'ex_N100_res5980' qui renvoit 4000).
Les fichiers avec 100000 données et plus représentent une trop grande quantité de données pour notre compléxité en ø(n²), ils n'ont donc pas été testés avec cet algorithme 

L'algorithme suivant se base sur la stratégie de diviser pour régner, son principe serait de couper la surface au point du milieu de la liste de point, calculer le rectangle maximum à gauche, celui à droite, sans oublier de calculer le rectangle le plus large qui 'chevaucherait' les 2 parties en ayant pour hauteur maximale le y du dit point. Pour calculer les rectangles des parties de gauche et droite on avance recursivement sur chaque partie de la même manière. Lorsqu'il ne reste que 2 ou 3 points dans notre récursion, on calcule en prime les rectangles ayant h comme hauteur et comme longueur la distance entre les 1er et 2e points et entre les 2e et 3e points.

Malheureusement nous n'avons pas reussi à faire fonctionner cet algorithme sur les jeux de données, le voici cependant dans son état actuel 

```python
def algo_div(l,h,points,g,d):
    m = (g+d)//2
    pointMid = points[m]
    xMid = pointMid[0] 
    yMid = pointMid[1]

    #first case when there is no more division coming
    if (d-g <= 2):
        return h * (points[m][0]-points[m-1][0])

    if (d-g == 3):
        return max((h * (points[m][0]-points[m-1][0])),(h * (points[m+1][0]-points[m][0])))
    #we first check the rectangle in between the two parts with y = ay, with ay the separating point 
    
    #look for first lower point on the left 
    leftIndex = m-1  
    leftLimit = pointMid
    while(leftLimit[1]>=yMid and leftIndex >=0):
        leftIndex -= 1
        leftLimit = points[leftIndex] 
    #look for first lower point on the right 
    rightIndex = m+1  
    rightLimit = pointMid
    while(rightLimit[1]>=yMid and rightIndex <= n ):
        rightIndex += 1
        rightLimit = points[rightIndex]
    midRect = (rightLimit[0]-leftLimit[0]) * yMid
    # we can now check max rectangle in each part 
    maxLeft = algo_div(l,h,points,g,m)
    maxRight = algo_div(l,h,points,m+1,d)
    return max(maxLeft,midRect,maxRight)

```
