# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:23:57 2020

@author: Julien
"""


import numpy as np

class Point :
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def dist(self, P):
        return (np.sqrt((self.x-P.x)**2+(self.y-P.y)**2))

def IsOrthogonal(a, b, c):
    return (b.x - a.x) * (b.x - c.x) + (b.y - a.y) * (b.y - c.y) == 0;


def is_rect(R):
    a,b,c,d = R[0],R[1],R[2],R[3]
    ans = True
    if a.dist(b) != c.dist(d) :
        ans = False
    if a.dist(d) != b.dist(c) :
        ans = False
    if not IsOrthogonal(d,a,b):
        ans = False
    if not IsOrthogonal(a,b,c):
        ans = False
    if not IsOrthogonal(b,c,d):
        ans = False
    if not IsOrthogonal(c,d,a):
        ans = False
    return(ans)

def is_min(R):
    a,b,c = R[0],R[1],R[2]
    return (a.dist(b)*b.dist(c) != 1)
    
count = 0

def find_rectangle(R):
    a,b,c,d = R[0],R[1],R[2],R[3]
    if is_min(R):
        return 1
    else :
        for i in range()
    
    
    
    


































