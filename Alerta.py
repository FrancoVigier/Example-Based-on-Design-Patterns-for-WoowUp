# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 13:49:34 2023

@author: usuario
"""
from abc import ABC, abstractmethod
from datetime import datetime
class Alerta(ABC):
    #Siempre tienen origen, pero dependiendo si es broadcast o no puede no haber un destino puntual
    def __init__(self,tema ,contenido, origen,year, month, day, hour, minute, second, destino = None):
        self.tema = tema
        self.contenido = contenido
        self.addPrefix()#Str polimorph porque se basa en addPrefix que cada hija la define indiv  
        self.origen = origen
        self.dataExpire = datetime(year, month, day, hour, minute, second)
        if not (isinstance(destino, type(None))):
            self.destino = destino
        else:
            self.destino = None
    
    def __str__(self):   
        #self.addPrefix() Si pongo aca muero porque cada vez que imprimo agrega el prefix
        s = "Alerta de " + self.origen.getNombre() + "\nTema: "+self.tema+"\n"+ self.contenido + "\nExpire Date: "+ str(self.dataExpire)
        if not (isinstance(self.destino, type(None))):
            s += "\nDestino: " + self.destino.getNombre() +"\n"
        else:
            s += "\nDestino: BroadCast para los interesados en el Tema\n"
        return s
    
    @abstractmethod
    def addPrefix(self):
        pass
    def getContenido(self):
        return self.contenido
    
    def getOrigen(self):
        return self.origen
    
    def getTema(self):
        return self.tema
    
    def getDataExpire(self):
        return self.dataExpire
    
    def getDestino(self):
        return self.destino
    
    def alertExpireYet(self):
        now = datetime.now()
        if 0 < now.timestamp() - self.dataExpire.timestamp() :
            return True
        return False
    
#le agrege un metodo banana para que difieran en algo
class Urgente (Alerta):
    def addPrefix(self):
        self.contenido = "Urgente: " + self.getContenido()
        
class Informativa(Alerta):
    def addPrefix(self):
        self.contenido = "Informativa: " + self.getContenido()
        