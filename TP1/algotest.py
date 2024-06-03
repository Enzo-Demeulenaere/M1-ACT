# trouver les 'top' (l = ymax), puis le reste

# top : 
#   - l = ymax
#   - liste des x
#   - pour chaque x : L = precedent -> next

# reste :
#   - pour chaque point: l = y, cherche last xi, next xj avec yi,yj > y

# à chaque fois qu'un rectangle est trouvé, compare sa taille avec le precedent

# format des data :
# xmax ymax
# nb points
# x1 y1
# x2 y2
# ...

bestRectangle = none
xmax = #lecture
ymax = #lecture
nbp = #lecture
points = ()
xList = ()
for i in range (nbp):
    points.append(*lecture*)
    xList.append(points(i))

currentx = 0
for i in xList:
    rect = ymax * i-currentx
    if rect > bestRectangle:
        bestRectangle= rect
    currentx = i
# top faits

prev = (0,0)
for i in range (len(points)-1):
    point = points(i)
    

