# Compte Rendu TP2 Programmation dynamique

## Question 1 

si il existe des successeurs négatifs : abs(maximum) +1, maximum <0

sinon : - (maximum+1)


structure de données possible :

pour chaque recursion, on créé une liste et un dictionnaire, lorsqu'on a calculé une configuration et un nombre de coups, on ajoute le nombre de coups à la liste à l'indice i et on ajoute dans le dictionnaire le couple (i -> configuration)

