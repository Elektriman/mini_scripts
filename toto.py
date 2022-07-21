# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 18:26:03 2021

@author: Julien
"""


def toto(n):
    if n==0 :
        return "( 0 + 0 )"
    else :
        t = toto(n-1)
        return f"( {t} + {t} )"

print(toto(4))