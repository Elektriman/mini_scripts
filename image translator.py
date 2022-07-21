# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:09:19 2020

@author: Julien
"""

"""
imports
"""
import numpy as np
import matplotlib.image as mpimg

#importation de l'image
img = mpimg.imread(input("nom de l'image : "))
img = np.array(img, dtype=int) #transformation en array d'entiers

#fonction qui va transformer une image rectangulaire en carré le plus grand possible et centré
def toSquare(img):
    if img.shape[0]>img.shape[1] :
        delta = img.shape[0]-img.shape[1]
        return img[delta//2:-delta//2]
    elif img.shape[0]<img.shape[1] :
        delta = img.shape[1]-img.shape[0]
        return img[:,delta//2:-delta//2]
    else :
        return img

img = toSquare(img)
#G est l'image en nuances de gris
G = np.zeros((img.shape[0],img.shape[1]))
G = (img[:,:,0]+img[:,:,1]+img[:,:,2])//3 #on fait la moyenne des composantes RGB
G = G.transpose() #on transpose car l'image est sur le côté

#N est l'image en noir et blanc, le seuil doit être adapté pour chaque image
N = G > 104

def parcours(G):
    #on vérifie si l'image a une seule couleur
    if((G == np.full((G.shape[0],G.shape[1]), True)).all()): #cas où tout est noir
        return "N"
    elif((G == np.full((G.shape[0],G.shape[1]), False)).all()): #cas où tout est blanc
        return "B"
    else : #sinon
        #(a,b) est le millieu du carré
        a = G.shape[0]//2
        b = G.shape[1]//2
        #on répète l'opération avec les quatres carrés créés lors de la subdivision
        I1 = parcours(G[:a,:b])
        I2 = parcours(G[a:,:b])
        I3 = parcours(G[:a,b:])
        I4 = parcours(G[a:,b:])
        return f"({I1}{I2}{I3}{I4})" #la chaine de caractère formattée avec les parenthèses

P = parcours(N) #on fabrique la chaine de caractères
    
with open("image string.txt", "w") as f: #ouverture/création d'un document texte
    n = f.write(P) #on l'écris dans notre bloc note/ document texte
    
    #vérification de l'écriture correcte
    if n!=len(P):
        print('erreur lors de l\'ecriture')
    else :
        print('ecriture reussie')