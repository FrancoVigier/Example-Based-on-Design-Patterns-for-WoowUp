# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 13:58:17 2023

@author: usuario
"""
from abc import ABC, abstractmethod

class Buzon(ABC):
    def __init__(self, msjs = []):
        self.buzon = msjs
    def __add__(self, other):
        return self.buzon + other.getBuzon()
    def agregarObj(self, Obj):
        self.buzon.append(Obj)
    def reversa(self):
        return self.buzon[::-1]
    def getBuzon(self):
        return self.buzon
    def getLen(self):
        return len(self.buzon)
    @abstractmethod
    def extraerObj(self):
        pass
    
class FIFO(Buzon): #info

    def extraerObj(self):
        return self.buzon.pop(0)
    
class LIFO(Buzon):#Urg
    def extraerObj(self):
        return self.buzon.pop()