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
n=n+1

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

print(algo_n2(x,y,points))