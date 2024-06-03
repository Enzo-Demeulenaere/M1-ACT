# principe : 
# couper au point du milieu
# calculer le max à gauche et à droite
# calculer le max du milieu
# pour le max du milieu : calculer avec le point du milieu comme hauteur
# calculer les rectangle avec hauteur h lorsqu'il reste qu'un point à gauche et/ou à droite

import sys

f = open(sys.argv[1],"r")
size = f.readline().split()
x = int(size[0])
y = int(size[1])
n = int(f.readline())
points = [[0,0]] 
for i in range (n) :
    line = f.readline()
    p = line.split()
    points.append([int(p[0]),int(p[1])])
points.append([x,y])


g = 0
d = n+2
bestRect = 0

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

print(algo_div(x,y,points,g,d))