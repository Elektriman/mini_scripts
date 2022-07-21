# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import numpy as np

#crible d'hérathosthène
def crible(n):
    C = np.full(n, True)
    C[:2] = False
    l = int(np.sqrt(n))
    i = 2
    while i<=l :
        if C[i] :
            for u in range(2*i,n,i):
                C[u]=False
        i+=1
    return(C)

N = 100
P = np.arange(N)[crible(N)]
a=0
for i in range(len(P)-1):
    print(P[i]-(i+1))
