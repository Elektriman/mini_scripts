# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:05:54 2020

@author: Julien
"""

"""
imports
"""
import random


"""
constants
"""

COLOR_BLUE = 0
COLOR_RED = 1
COLOR_GREEN = 2

"""
classes
"""

class Vertice :
    #static
    numVertices = 0
    
    #attributes
    num = 0
    x = 0
    y = 0
    color = -1
    degree = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Vertice.numVertices += 1
        self.num = Vertice.numVertices
    
    def setColor(self, c):
        self.color = c
    
    def toString(self):
        return "V"+str(self.num)
    
    def setDegree(self, d):
        self.degree = d
    
    def getDegree(self):
        return self.degree


"""
main program
"""

random.seed(17)
N = 10
V = [Vertice(0,0) for i in range(N)]
E = []

while len(E)<7 :
    a = random.randint(0,9)
    b = random.randint(0,9)
    if a!=b :
        new = (V[a],V[b])
        other = (V[b],V[a])
        if not (new in E or other in E) :
            E.append(new)

for v in V:
    print(v.toString())
for e in E:
    print("({},{})".format(e[0].toString(), e[1].toString()))

for e in E:
    e[0].setDegree(e[0].getDegree() + 1);
    e[1].setDegree(e[1].getDegree() + 1);

for v in V:
    print(v.toString(),v.getDegree())
