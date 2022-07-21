# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:31:30 2020

@author: Julien
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

"""
initialisations des variables
"""

N = 50

A = np.arange(1, N) #1,2,3,4,5,6...
B = np.arange(3, N+3, 2) #3,5,7,9,11,13...
C = -2*(np.arange(N)//2 % 2)+1 #1,1,-1,-1,1,1,-1,-1,...
D = np.zeros(N, dtype=int)

"""
construction du premier tableau
1,3,2,5,3,7,4,... == A[0],B[0],A[1],B[1],A[2],B[2],...
"""

for i in range(len(D)):
    if i%2==0 :
        D[i]=A[i//2]
    else :
        D[i]=B[i//2]

"""
construction du tableau intermédiaire
E = 1, 4, 6, 11, 14, ...
"""

E = [1]
for i in range(len(D)):
    E.append(E[-1]+D[i])

E = np.array(E)

"""
construction du tableau avec les plus et les moins
F = 1,1,0,0,-1,0,-1,...
"""

F = np.zeros(N)
i=0
while E[i]-1 < N :
    F[E[i]-1]=C[i]
    i+=1

"""
construction du tableau final
G = 1, 1, 2, 3, 5, 7, 11, 15 ...
"""

G = [1]
for i in range(N):
    n = len(G)
    U = np.flip(F[:n])
    G.append((G*U).sum())
    
G = np.array(G, dtype=int)

print(G)

"""
construction du deuxième tableau
->compteur des sommes des facteurs de n
"""

H = [1]
for i in range(N):
    H[0]=i+1
    n = len(H)
    U = np.flip(F[:n])
    H.append((H*U).sum())
    
H = np.array(H[1:], dtype=int)

print(H)





















