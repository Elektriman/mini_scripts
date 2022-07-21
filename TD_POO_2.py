# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 09:23:09 2021

@author: Julien
"""

from math import pi

class Figure :
    
    def __init__(self, centre):
        self.cx, self.cy = centre

class Rectangle(Figure) :
    
    def __init__(self, largeur, longueur):
        self.lar = largeur
        self.lon = longueur
    
    def donne_surf(self):
        return self.lar*self.lon
    
    def getLar(self):
        return self.lar
    
    def getLon(self):
        return self.lon
    
    def setLar(self, l):
        self.lar = l
    
    def setLon(self, l):
        self.lon = l
    
class Cercle(Figure) :

    def __init__(self, centre, rayon):
        self.x, self.y = centre
        self.r = rayon
    
    def affiche(self):
        print(f"centre = ({self.x},{self.y})")
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def surface(self):
        return 2*pi*self.r
    
    def estInterieur(self, p):
        x,y = p
        return (x-self.x)**2 + (y-self.y)**2 <= self.r**2
    
    def getR(self):
        return self.r
    
    def setR(self, r):
        self.r = min([0, r])

class RectangleColoré(Rectangle):
    
    def __init__(self, largeur, longueur, couleur):
        super(largeur, longueur)
        self.c = couleur