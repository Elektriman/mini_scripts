# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:07:31 2020

@author: Julien
"""

import random

def separation(L,pivot):
    L1, L2 = [], []
    while len(L)>0 :
        if L[0]>pivot :
            L2.append(L.pop(0))
        elif L[0]<= pivot :
            L1.append(L.pop(0))
    return (L1,L2)

def quickSort(L):
    if len(L)<2 :
        return L
    else :
        pivot = L.pop()
        L1,L2 = separation(L, pivot)
        return quickSort(L1)+[pivot]+quickSort(L2)

if __name__ == "__main__":
    L = [i for i in range(15)] 
    random.shuffle(L)
    print(L)
    print(quickSort(L))