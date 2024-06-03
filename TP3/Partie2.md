# Partie 2 : Réductions polynomiales

## 1 

Partition se réduit polynomialement en BinPack car l'on peut transformer Partition en l'instance suivante :

on possède n objets de poids xi, on essaie de les répartir dans 2 sacs de capacité maximales c = (1/2)*somme(xi , ic[1,n])

### 1.1 

```python
def reductionPartitionBinPack(n,l):
    weight = l
    k = 2 
    capacity = sum(l)/2

    return n, weight, k ,capacity
```

### 1.2 

BinPack est par conséquent NP-Dur car Partition étant NP-Dur peut se réduire polynomialement en BinPack

### 1.3 

BinPack ne semble pas pouvoir se réduire polynomialement en Partition, cela voudrait signifier que les propriétés sont égales car elles pourraient mutuellement se réduire polynomialement en l'autre.

## 2 

Partition pourrait être perçu comme un cas particulier de Sum dans le cas où c est égal à la moitié de la somme des xi, En terme de réduction on peut donc supposer que Sum se réduit polynomialement en Partition.

## 3 

Sum se réduit polynomialement en Partition car l'on peut transformer Sum en l'instance suivante: 

Soit I une instance de Sum, on possède alors n entiers de valeurs xi et un entier c. 
Transformons I en red(I)

Soit L1 la liste contenant les n entiers xi, ajoutons à cette liste un entier k de sorte que la somme des xi + k soit égale à 2c.
Nous obtenons une liste L2 contenant n+1 entiers ce qui constitue des données valides en entrée de Partition.

Si I est valide, alors il existe un sous-ensemble d'entiers dont la somme vaut c, les entiers non compris dans cet ensemble ont une somme totale valant S-c, en ajoutant un entier k tel que S+k = 2c, on obtient bien une instance red(I) depuis laquelle on peut extraire un sous-ensemble dont la somme vaudra la moitié de la somme totale des entiers.

Si red(I) est valide, alors il existe 2 sous-ensembles dont la somme totale vaut c, parmi ces sous-ensembles l'un ne possède pas un l'entier qui correspond à l'entier k valant 2c-S, ce sous-ensemble formera donc un sous-ensemble solution pour l'instance I qui est par conséquent valide.

Ainsi nous avons prouvé que Sum se réduit polynomialement en Partition


```python
def reductionSumPartition(n,l,c):
    sumL = sum(l)
    l.append(2*c-sumL)
    return n+1,l 
```

## 4 

Pour implémenter une réduction de Sum dans BinPack, il suffit d'utiliser la sortie de la réduction de Sum dans Partition comme entrée pour la réduction de Partition dans BinPack

```python
def reductionSumBinPack(n,l,c):
    nextN,nextL = reductionSumPartition(n,l,c)
    return reductionPartition(nextN,nextL)
```
