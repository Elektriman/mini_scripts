# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 08:55:02 2021

@author: Julien
"""


class complexe :
    
    def __init__(self, reel=0, imag=0):
        self.reel = reel
        self.imag = imag
    
    def getR(self):
        return self.reel
    
    def getI(self):
        return self.imag
    
    def addition_p(self, c):
        ad_reel = self.getR()+c.getR()
        ad_imag = self.getI()+c.getI()
        return complexe(ad_reel, ad_imag)
    
    @staticmethod
    def addition_s(c1, c2):
        ad_reel = c1.getR()+c2.getR()
        ad_imag = c1.getI()+c2.getI()
        return complexe(ad_reel ,ad_imag)
    
    def mult_reel(self, k):
        return complexe(self.getR()*k, self.getI()*k)
    
    def mult_cplx(self, c):
        return complexe(self.getR()*c.getR()-self.getI()*self.getI(), self.getR()*c.getI()+self.getI()*c.getR())
    
    def toString(self):
        return f'({self.getR()} + {self.getI()}i)'
    

if __name__ == '__main__' :
    c1 = complexe(1,2)
    c2 = complexe()
    c3 = complexe(2,3)
    print('c1 = '+c1.toString())
    print('c2 = '+c2.toString())
    print('c1+c2 = '+c1.addition_p(c2).toString())
    print('c1+c2 = '+complexe.addition_s(c1, c2).toString())
    print('c1*5 = '+c1.mult_reel(5).toString())
    print('c1*c3 = '+c1.mult_cplx(c3).toString())