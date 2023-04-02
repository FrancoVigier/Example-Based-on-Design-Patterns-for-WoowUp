# -*- coding: utf-8 -*-
"""
Created on Sat Abr 01 04:15:33 2023

@author: usuario
"""
import Alerta
import Buzon
class Cliente():
    def __init__(self, nombre, Id, admEventos, buzonUrg, buzonInfo, buzonLeidos):
        self.nombre = nombre
        self.id = Id
        self.adm = admEventos
        #Puedo componer con un Obj Buzon de otra clase pero no lo voy a hacer
        #asi que tenemos la nefasta implementacion como arrays, asumo que no 
        #va a cambiar, sino tengo que abstraer con un nivel mas la implementacion
        self.BuzonAlertasUrg = buzonUrg
        self.BuzonAlertasInfo = buzonInfo #stack push pop
        self.BuzonAlertasLeidas = buzonLeidos
        
    def __str__(self):
        movStr1 = '\n'.join(map(str, self.BuzonAlertasUrg.getBuzon()))
        movStr2 = '\n'.join(map(str, self.BuzonAlertasInfo.getBuzon()))
        movStr3 = '\n'.join(map(str, self.BuzonAlertasLeidas.getBuzon()))
     
        s = "Cliente: " + str(self.id) + "\nNombre: " + str(self.nombre)
        s += "\nBuzon Urgente: \n"+movStr1
        s += "\nBuzon Informativo: \n"+movStr2
        s += "\nBuzon Leidos: \n"+movStr3
        return s
    
    def getNombre(self):
        return self.nombre
    def getId(self):
        return self.id
    def getAdm(self):
        return self.adm
    def getBA(self, buzon = 0):
        if buzon == 0:
            return self.BuzonAlertasUrg #Obj Buzon
        return self.BuzonAlertasInfo
   
    def getBAL(self):
        return self.BuzonAlertasLeidas
    def addBA(self,AlertaObj, buzon = 0): #0 es Urg
        if buzon == 0:
            return self.BuzonAlertasUrg.agregarObj(AlertaObj)
        return self.BuzonAlertasInfo.agregarObj(AlertaObj)
        
    def addBAL(self,AlertaObj):
        self.BuzonAlertasLeidas.agregarObj(AlertaObj)
        
    def leer(self, buzon = 0):
        if buzon == 1 and 1 <= self.BuzonAlertasInfo.getLen(): #leemos de la informativa
            AI = self.BuzonAlertasInfo.extraerObj()
            self.addBAL(AI)
            return AI
        if buzon == 0 and 1 <= self.BuzonAlertasUrg.getLen():
            AU = self.BuzonAlertasUrg.extraerObj()
            self.addBAL(AU)
            return AU
        
        
    def obtenerAlertasNoExpiradasNoLeidas(self, temaStr = None):
        UrgList = Buzon.LIFO(msjs = [])
        InfList = Buzon.FIFO(msjs = [])

        for alert in self.BuzonAlertasUrg.reversa():
            if not alert.alertExpireYet():
                if isinstance(temaStr, type(None)):
                    UrgList.agregarObj(alert)
                elif(alert.getTema() == temaStr):
                    UrgList.agregarObj(alert)

        for alert in self.BuzonAlertasInfo.getBuzon():
            if not alert.alertExpireYet():
                if isinstance(temaStr, type(None)):
                    InfList.agregarObj(alert)
                elif(alert.getTema() == temaStr):
                    InfList.agregarObj(alert) 
                    
        if isinstance(temaStr, type(None)):
            return (UrgList + InfList) #Suma de Obj Buzon es una LISTA
        else:
            return UrgList,InfList #Tupla de Obj Buzon, son 2 obj buzon
        
    def obtenerAlertasNoExpiradasTema(self, temaStr):
        U = Buzon.LIFO(msjs = [])
        I = Buzon.FIFO(msjs = [])
        for alert in self.BuzonAlertasLeidas.getBuzon():
            if alert.getTema() == temaStr:
                if isinstance(alert, Alerta.Urgente):
                    U.agregarObj(alert)
                if isinstance(alert, Alerta.Informativa) :
                    I.agregarObj(alert)
        UNL, INL = self.obtenerAlertasNoExpiradasNoLeidas(temaStr = temaStr)
        #si bien usr.getDestino().getNombre() es self.getNombre() lo dejo asi para ver que el nombre del destino e el mio. getDestino es un Cliente
        L = map( (lambda usr : (usr, "BroadCast") if isinstance(usr.getDestino(), type(None) ) else (usr,"P2P to: "+ usr.getDestino().getNombre())), (U.getBuzon() + UNL.getBuzon() + I.getBuzon() + INL.getBuzon()))
        return list(L)
    
    #p2p el id del que mandamos
    #Invocacion implicita al usar anunciarAlerta del Adm, esta va a fijarse los
    #suscritos al tema de la alerta misma y se lo manda. Si es p2p no importa fijarse
    #y manda igual
    def clienteEnviarAlerta(self,AlertaObj):
        if not (isinstance(AlertaObj.getDestino(), type(None))) :
            self.adm.anunciarAlerta(AlertaObj, self ,destinoUsr = AlertaObj.getDestino())
        else:
            self.adm.anunciarAlerta(AlertaObj, self)
    #invocacion implicita al admEventos pero no se fija en los suscritos al evento
    #RegistrarTema porque todos pueden hacerlo trivial
    def clienteRegistarmeATema(self, TemaStr, allTopics = 0): #OK
            self.adm.anunciarRegistroTema(self,TemaStr, todos = allTopics)
            
   # def clienteDesRegistarmeATema(self, TemaStr):
   #         self.adm.anunciarDesRegistroTema(self,TemaStr)
    
    def clienteObtenerListaDeTemas(self): #OK
        return self.adm.anunciarListaTemasPermitidos(self) #[TemaStr]
    
    def clienteRegistrarNuevoTema(self, TemaStr): #OK
            self.adm.anunciarNewTema(self.getId(),TemaStr)
            
    def clienteRegistrarme(self, privativo = 0): #OK
        self.adm.suscribirNewUser(self, privativo = privativo)
        self.adm.anunciarNewUser(self)
        
    def clienteRegistrarmeConTodasSuscripcion(self): #OK
        self.adm.suscribirClienteATodoEvento(self)


        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    