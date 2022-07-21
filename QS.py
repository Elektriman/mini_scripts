# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 18:07:47 2021

@author: Julien
"""

import numpy as np

np.random.seed(69)

def mix(L):
    for i in range(100):
        a,b = np.random.randint(0,len(L)),np.random.randint(0,len(L))
        L[a],L[b] = L[b],L[a]

def QuickSort(L):
    i=len(L)-1
    place=[]
    a=0
    for k in range(len(L)):
        while i!=a:
            if (L[i]<L[a] and i>a) or (L[i]>L[a] and i<a):
                L[i],L[a]=L[a],L[i]
                a,i=i,a
            if i<a:
                i+=1
            else:
                i-=1
        place.append(a)
        if a-1 in place:
            a=max(place)+1
            i=len(L)-1
        elif a>=0:
            a-=1
            i=a-1

# L = [np.random.randint(20) for i in range(20)]
# print(L)
# QuickSort(L)
# print(L)

def QS(L):
    a,b = 0, len(L)-1
    curseur = True
    while a<b :
        
        if L[a]>L[b] :
            L[a],L[b] = L[b],L[a]
            
            curseur = not curseur
        
        if curseur :
            b-=1
        else :
            a+=1
    
    if len(L)>1 :
        return(QS(L[:a]) + [L[a]] + QS(L[a+1:]))
    else :
        return(L)

def mix(L):
    for i in range(100):
        a,b = np.random.randint(0,len(L)),np.random.randint(0,len(L))
        L[a],L[b] = L[b],L[a]
        
L = [i for i in range(20)]
mix(L)
print(QS(L))
























