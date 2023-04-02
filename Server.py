# -*- coding: utf-8 -*-
"""
Created on Sat Abr 01 04:15:45 2023


@author: usuario
"""
import Alerta
from abc import ABC


class Servidor(ABC):
    def __init__(self, l1 = [], l2 = [], l3 = {}, l4 = [],
                 l5 = [], l6 = [], l7 = {}, l8 = [], l9 = [], l10 = []):
        self.RegTemas = l1 #TemasStr
        self.RegUsers = l2 #User
        self.SuscripcionTemas = l3 #Tema:[User]
        self.SuscripcionOperaciones = {'Registrarse' : l4, #ok
                                       'DesRegistrarse' : l5,
                                       'RegistrarTema' : l6, #ok
                                       'DesRegistrarTema' : l7,
                                       'AnunciarAlerta' : l8, #ok
                                       'SuscribirATema' : l9, #ok
                                       'DarListaTemas' : l10} #ok
        
    def __str__(self):
        movStr1 = '\n'.join(map(str, self.RegUsers))
        s = "Usuarios Registrados:\n " + movStr1 + "\n" 
        movStr2 = '\n'.join(map(str, self.RegTemas))
        s += "Temas Registrados: " + movStr2 + "\n"
        s += "Tabla De Suscripciones a Temas: "+ str(self.SuscripcionTemas) + "\n"
        s += "Tabla De Suscripciones a Operaciones: " + str(self.SuscripcionOperaciones) + "\n" 
        return s
        
    def suscribirClienteATodoEvento(self, user):
        #Siempre el cliente primero se suscribe y luego se anuncia al evento
        self.suscribirNewUser(user, privativo = 0)
        self.anunciarNewUser(user)
        
        self.suscribirNewTema(user)
        self.suscribirListaTemasPermitidos(user)
        self.suscribirRegistroTema(user)
        self.suscribirAnunciarAlerta(user)
        
        
        
    def userInRegistrados(self,user):
        idUser = user.getId()
        for usr in self.RegUsers: #Si no esta el usuario reg
            if usr.getId() == idUser:
                return True
        return False
        
        ###Par anuncio del Evento NewUser y suscribir. Primero Me ME SUSCRIBO Y LUEGO REGISTRO
    def anunciarNewUser(self,user):
        idUser = user.getId()
         # y esta en la lista de los posibles permitidos a registrar lo meto
        for suscriptorRegistrarse in self.SuscripcionOperaciones['Registrarse']:
            if(idUser == suscriptorRegistrarse):
                self.RegUsers.append(user)
    def suscribirNewUser(self,user, privativo = 0):
        idUser = user.getId()
        if not self.userInRegistrados(user):
            if privativo == 0:
                if idUser not in self.SuscripcionOperaciones['Registrarse']:
                    self.SuscripcionOperaciones['Registrarse'].append(idUser)
            if privativo != 0:
                if idUser in self.SuscripcionOperaciones['Registrarse']:
                    self.SuscripcionOperaciones['Registrarse'].append(idUser)

            
        ###Par anuncio del Evento RegistrarNuevoTema
    def anunciarNewTema(self,userId,TemaStr):
        if (TemaStr not in self.RegTemas) and (userId in self.SuscripcionOperaciones['RegistrarTema']) :
            self.RegTemas.append(TemaStr)
            self.SuscripcionTemas[TemaStr] = []
            
    def suscribirNewTema(self, user):
        idUser = user.getId()
        if self.userInRegistrados(user):
            if idUser not in self.SuscripcionOperaciones['RegistrarTema']:
                self.SuscripcionOperaciones['RegistrarTema'].append(idUser)
        ###Par anuncio del Evento ObtenerListaTemas
    def anunciarListaTemasPermitidos(self,user):
        idUser = user.getId()
        if idUser in self.SuscripcionOperaciones['DarListaTemas']:
            return self.RegTemas
        
    def suscribirListaTemasPermitidos(self, user):
        idUser = user.getId()
        if self.userInRegistrados(user):
            if idUser not in self.SuscripcionOperaciones['DarListaTemas']:
                self.SuscripcionOperaciones['DarListaTemas'].append(idUser)
            
        ###Par anuncio del Evento RegistarmeATema
    def anunciarRegistroTema(self,user,TemaStr, todos = 0):
        idUser = user.getId()
        if todos != 0:
            if idUser in self.SuscripcionOperaciones['SuscribirATema']:
                for tema in self.RegTemas:
                    if idUser not in self.SuscripcionTemas[tema]:
                        self.SuscripcionTemas[tema].append(idUser) #(Tema:Id)
        
        elif (TemaStr in self.RegTemas):
            if idUser in self.SuscripcionOperaciones['SuscribirATema'] and idUser not in self.SuscripcionTemas[TemaStr] :
                self.SuscripcionTemas[TemaStr].append(idUser) #(Tema:Id)
                
    def suscribirRegistroTema(self, user):
        idUser = user.getId()
        if self.userInRegistrados(user):
            if idUser not in self.SuscripcionOperaciones['SuscribirATema'] :
                self.SuscripcionOperaciones['SuscribirATema'].append(idUser)
        ###Par anuncio del Evento EnviarAlerta
    
    def anunciarAlerta(self, AlertaObj, origenUsr ,destinoUsr = None):
        origenId = origenUsr.getId()

        if origenId in self.SuscripcionOperaciones['AnunciarAlerta'] and AlertaObj.getTema() in self.RegTemas:
            if(isinstance(AlertaObj, Alerta.Urgente)):
                if (isinstance(destinoUsr, type(None))):
                    for usr in self.RegUsers:
                        if usr.getId() in self.SuscripcionTemas[AlertaObj.getTema()] :
                            usr.addBA(AlertaObj, buzon = 0)
                else:
                    destinoUsr.addBA(AlertaObj,buzon = 0)
            if(isinstance(AlertaObj, Alerta.Informativa)):
                if (isinstance(destinoUsr, type(None))):
                    for usr in self.RegUsers:
                        if usr.getId() in self.SuscripcionTemas[AlertaObj.getTema()]:
                            usr.addBA(AlertaObj, buzon = 1)
                else:
                    destinoUsr.addBA(AlertaObj,buzon = 1)
                    
    def suscribirAnunciarAlerta(self,user):
        idUser = user.getId()
        if self.userInRegistrados(user):
            if idUser not in self.SuscripcionOperaciones['AnunciarAlerta']:
                self.SuscripcionOperaciones['AnunciarAlerta'].append(idUser)

    def getRegUser(self):
        return self.RegUsers
    def getRegTemas(self):
        return self.RegTemas
    def getSuscripcionOperaciones(self):
        return self.SuscripcionTemas
            
        
            
            
            
            
            
            
            
            
            