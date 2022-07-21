# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:24:11 2020

@author: Julien
"""


import numpy as np

def crible(n):
    C = np.full(n, True)
    C[:2] = False
    i = 2
    while i<=int(np.sqrt(n)) :
        if C[i] :
            for u in range(2*i,n,i):
                C[u]=False
        i+=1
    return(C)

N=100000
Primes = np.arange(N)[crible(N)]

def suivant(c):
    return int(c)*(c-int(c)+1)

def BAconst(n):
    global Primes
    S = 0
    for i in range(n, min(n+10,len(Primes))):
        product=1
        for j in range(n,i):
            product*=Primes[j]
        S+=(Primes[i]-1)/product
    return S

print(BAconst(0))
























