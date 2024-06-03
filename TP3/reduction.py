def reduction(n,l,c):
    sumL = sum(l)
    for i in range(n):
        l[i]=2*sumL*l[i]/c

    return n,l 