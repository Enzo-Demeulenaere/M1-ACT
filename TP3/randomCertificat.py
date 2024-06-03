
import random

def randomCertificat(n,k):
    rep = []
    for i in range(n):
        rep.append(random.randint(1,k))
    return rep

print(randomCertificat(15,5))