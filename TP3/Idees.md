# Partie 2 : Réductions polynomiales

## 1 

Partition se réduit polynomialement en BinPack car l'on peut transformer Partition en l'instance suivante :

on possède n objets de poids xi, on essaie de les répartir dans 2 sacs de capacité maximales c = (1/2)*somme(xi , ic[1,n])

## 1.1 

```python
def reduction(n,l):
    weight = l
    k = 2 
    capacity = sum(l)/2

    return n, weight, k ,capacity
```

## ILS 

le but: appliquer des perturbations et les accepter (ou non) pour approcher l'optimale

Il faut determiner: 

    - un type de perturbations (voisinage/nombre)
    - un critère d'acceptation (comparaison directe/quelques itérations de recherche)
    - un critère d'arret (temps d'execution/nombre de perturbation)

5 repetitions, 10 swaps

100-15 -> (173554, 4.4521484375)
100-16 -> (409188, 1.3806653022766113)
100-17 -> (332939, 1.2912399768829346)
100-18 -> (545081, 3.0349082946777344)
100-19 -> (478587, 3.1444714069366455)
100-35 -> (19114, 1.34031343460083)
100-36 -> (110508, 1.185004711151123)
100-37 -> (183908, 2.323143243789673)
100-38 -> (91044, 1.1681253910064697)
100-39 -> (154015, 1.183440923690796)
100-40 -> (130313, 1.1940746307373047)
100-41 -> (464280, 1.5084459781646729)
100-42 -> (426789, 1.4833524227142334)
100-43 -> (322551, 1.3633413314819336)
100-44 -> (362478, 1.357978343963623)
100-85 -> (341, 1.0585317611694336)
100-86 -> (71244, 1.3312737941741943)
100-87 -> (88228, 2.1930551528930664)
100-88 -> (57872, 2.3547592163085938)
100-89 -> (56457, 1.1987080574035645)
1000-1 -> (663888774, 4869.563187360764)
1000-2 -> (688857988, 3349.598372936249)


Une autre ILS a plusieurs critères différents: le premier est sa perturbation qui consiste à un swap aléatoire de 2 elements avec un nombre choisi de 5 swaps aléatoires. Le critère d'acceptation est simple, on garde la meilleure solution entre la recherche locale et la recherche locale après perturbation. Cette ILS s'arrête après un total de 5 perturbations consécutives n'apportant aucune amélioration.

pourcentage moyen :  0.03144934878993798
temps moyen:  2.360936141014099
--
pourcentage moyen :  0.046555790930817166
temps moyen:  2.2349747896194456
--
pourcentage moyen :  0.03000254648270053
temps moyen:  2.3522191882133483
--
pourcentage moyen :  0.05359722893511476
temps moyen:  2.1312528014183045
--
pourcentage moyen :  0.05397776904676872
temps moyen:  2.377146327495575
--
pourcentage moyen final : 0.04311653683706783
temps moyen final : 2.2913058495521548

paramètres : seconde ILS avec 10swaps de perturbations, 5perturbations non-amélliorantes consécutives comme condition d'arrêt
