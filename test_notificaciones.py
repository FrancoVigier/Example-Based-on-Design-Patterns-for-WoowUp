# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 20:04:50 2023

@author: usuario
"""

import Cliente
import Server
import Alerta
import Buzon

import unittest
from parameterized import parameterized

class TestUtils(unittest.TestCase):
 #   @parameterized.expand([
 #       [100.0, 123456789, 987654321]
 #   ])
    def test_Punto1_Registro(self):
        #creamos el Adm
        AdmEventos = Server.Servidor()
        ###Creamos Los buzones de cada Usuario
            #Buzon Messi
        B1M = Buzon.LIFO(msjs = [])
        B2M = Buzon.FIFO(msjs = [])
        B3M = Buzon.FIFO(msjs = [])
        #Creamos un usuario
        Cliente1 = Cliente.Cliente("Messi", 1, AdmEventos,B1M,B2M,B3M)
        #Registramos
        Cliente1.clienteRegistrarmeConTodasSuscripcion()
        #El registrado este en el ADM
        self.assertTrue(Cliente1.getId() in map (lambda usr: usr.getId(),AdmEventos.getRegUser()) )
    
    def test_Punto2_Registro(self):
        #creamos el Adm
        AdmEventos = Server.Servidor()
        ###Creamos Los buzones de cada Usuario
            #Buzon Messi
        B1M = Buzon.LIFO(msjs = [])
        B2M = Buzon.FIFO(msjs = [])
        B3M = Buzon.FIFO(msjs = [])
        #Creamos un usuario
        Cliente1 = Cliente.Cliente("Messi", 1, AdmEventos,B1M,B2M,B3M)
        #Registramos
        Cliente1.clienteRegistrarmeConTodasSuscripcion()
        #Registramos el tema
        Cliente1.clienteRegistrarNuevoTema("Motos")
        self.assertTrue("Motos" in AdmEventos.getRegTemas())
        
    def test_Punto3_Suscripcion(self):
        #creamos el Adm
        AdmEventos = Server.Servidor()
        ###Creamos Los buzones de cada Usuario
            #Buzon Messi
        B1M = Buzon.LIFO(msjs = [])
        B2M = Buzon.FIFO(msjs = [])
        B3M = Buzon.FIFO(msjs = [])
        #Creamos un usuario
        Cliente1 = Cliente.Cliente("Messi", 1, AdmEventos,B1M,B2M,B3M)
        #Registramos
        Cliente1.clienteRegistrarmeConTodasSuscripcion()
        #Registramos los temas
        Cliente1.clienteRegistrarNuevoTema("Motos")
        Cliente1.clienteRegistrarNuevoTema("Autos")
        #Ponemos la suscripcion
        Cliente1.clienteRegistarmeATema("Autos")
        self.assertTrue(Cliente1.getId() in AdmEventos.getSuscripcionOperaciones()["Autos"])   
        self.assertTrue(Cliente1.getId() not in AdmEventos.getSuscripcionOperaciones()["Motos"])   
 
    def test_Punto4_y_Punto5_EnvioBroadcastUnicast(self):
        #creamos el Adm
        AdmEventos = Server.Servidor()
        ###Creamos Los buzones de cada Usuario
            #Buzon Messi
        B1M = Buzon.LIFO(msjs = [])
        B2M = Buzon.FIFO(msjs = [])
        B3M = Buzon.FIFO(msjs = [])
            #Buzon Diego
        B4M = Buzon.LIFO(msjs = [])
        B5M = Buzon.FIFO(msjs = [])
        B6M = Buzon.FIFO(msjs = [])
            #Buzon Riquelme
        B7M = Buzon.LIFO(msjs = [])
        B8M = Buzon.FIFO(msjs = [])
        B9M = Buzon.FIFO(msjs = [])
        #Creamos un usuario
        Cliente1 = Cliente.Cliente("Messi", 1, AdmEventos,B1M,B2M,B3M)
        Cliente2 = Cliente.Cliente("Maradona", 2, AdmEventos,B4M,B5M,B6M)
        Cliente3 = Cliente.Cliente("Riquelme", 3, AdmEventos,B7M,B8M,B9M)
        
        Cliente1.clienteRegistrarmeConTodasSuscripcion()
        Cliente2.clienteRegistrarmeConTodasSuscripcion()
        Cliente3.clienteRegistrarmeConTodasSuscripcion()
        #Creamos Las Alertas que Van a mandar los Users
            #Las alertas que va a mandar messi
        Alerta1 = Alerta.Urgente("Autos","Citroen Berlingo Casi Nueva 6000USD", Cliente1, 2023, 6, 1, 12, 24, 33)
        #Registramos los temas
        Cliente1.clienteRegistrarNuevoTema("Motos")
        Cliente2.clienteRegistrarNuevoTema("Autos")
        
        #Solo Diego y a Riquelme le va a interesar los autos
        Cliente2.clienteRegistarmeATema("Autos")
        Cliente3.clienteRegistarmeATema("Autos")
        #A riquelme ademas le gustan las motos
        Cliente3.clienteRegistarmeATema("Motos")
        #______________________________BroadCast Selectivo1___________
        #Messi Manda de Autos
        Cliente1.clienteEnviarAlerta(Alerta1)
        #Nos fijamos que diego y riquelme tengan la notificacion de messi en el buzon de urgentes
        self.assertTrue(Cliente1.getId() in map (lambda alert : alert.getOrigen().getId(),Cliente2.getBA(buzon = 0).getBuzon() ) )
        self.assertTrue(Cliente1.getId() in map (lambda alert : alert.getOrigen().getId(),Cliente3.getBA(buzon = 0).getBuzon() ) )
        #_______________________________BroadCast Selectivo2___________
        #Alerta de motos        
        Alerta2 = Alerta.Urgente("Motos","C90", Cliente1, 2023, 6, 1, 12, 24, 33)
        #Messi Manda de Motos
        Cliente1.clienteEnviarAlerta(Alerta2)
        #Nos fijamos que diego NO TENGA DE MOTOS y riquelme SI TENGA la notificacion de messi SOBRE MOTOS en el buzon de urgentes
            #Diego no tiene que tener un Mensaje de Messi de Motos
        self.assertTrue((Cliente1.getId(),"Motos", "Urgente: C90")  not in map (lambda alert : (alert.getOrigen().getId(), alert.getTema() , alert.getContenido()),Cliente2.getBA(buzon = 0).getBuzon() ) )
            #Riquelme si tiene que tener una alerta de messi sobre motos
        self.assertTrue((Cliente1.getId(),"Motos", "Urgente: C90") in map (lambda alert : (alert.getOrigen().getId(), alert.getTema(), alert.getContenido()),Cliente3.getBA(buzon = 0).getBuzon() ) )
        #_____________________________________UNICAST_________________
        #Alerta de Autos, SOLO PARA DIEGO
        Alerta3 = Alerta.Informativa("Autos","Ferrari F40 Negra Solo Diegote", Cliente1, 2023, 6, 1, 12, 24, 33, destino = Cliente2)
        #Messi Manda la oferta a DIEGO
        Cliente1.clienteEnviarAlerta(Alerta3)
        #Aunque riquelme y maradona esten suscritos a Autos solo le llega a diego
            #DiegoTiene su FERRARI
        self.assertTrue((Cliente1.getId(),Alerta3.getTema(), Alerta3.getContenido()) in map (lambda alert : (alert.getOrigen().getId(), alert.getTema(), alert.getContenido()),Cliente2.getBA(buzon = 1).getBuzon() ) )
            #Riquelme NO
        self.assertTrue((Cliente1.getId(),Alerta3.getTema(), Alerta3.getContenido()) not in map (lambda alert : (alert.getOrigen().getId(), alert.getTema(), alert.getContenido()),Cliente3.getBA(buzon = 1).getBuzon() ) )
     
    def test_Punto8_Leer(self):
         #creamos el Adm
         AdmEventos = Server.Servidor()
         ###Creamos Los buzones de cada Usuario
             #Buzon Messi
         B1M = Buzon.LIFO(msjs = [])
         B2M = Buzon.FIFO(msjs = [])
         B3M = Buzon.FIFO(msjs = [])
             #Buzon Diego
         B4M = Buzon.LIFO(msjs = [])
         B5M = Buzon.FIFO(msjs = [])
         B6M = Buzon.FIFO(msjs = [])
         #Creamos un usuario
         Cliente1 = Cliente.Cliente("Messi", 1, AdmEventos,B1M,B2M,B3M)
         Cliente2 = Cliente.Cliente("Maradona", 2, AdmEventos,B4M,B5M,B6M)
         
         Cliente1.clienteRegistrarmeConTodasSuscripcion()
         Cliente2.clienteRegistrarmeConTodasSuscripcion()
         
         #Creamos Las Alertas que Van a mandar los Users
             #Las alertas que va a mandar messi
         Alerta1 = Alerta.Urgente("Autos","Citroen Berlingo Casi Nueva 6000USD", Cliente1, 2023, 6, 1, 12, 24, 33)
         #Registramos los temas
         Cliente1.clienteRegistrarNuevoTema("Motos")
         Cliente2.clienteRegistrarNuevoTema("Autos")
         
         #Solo Diego le va a interesar los autos
         Cliente2.clienteRegistarmeATema("Autos")
         
         #Messi Manda de Autos
         Cliente1.clienteEnviarAlerta(Alerta1)
         #Diego LEE SU BUZON DE URGENTE
         AlertaLeida = Cliente2.leer(buzon = 0)
         #El buzon de Urgentes de diego ahora es VACIO
         self.assertTrue(Cliente2.getBA(buzon = 0).getLen() == 0)
         #El buzon de Leidos del Diego tiene 1 alerta la de messi
         self.assertTrue(Cliente2.getBAL().getLen() == 1)
         #En el buzon de leidos hay una alerta como la que retornamos
         self.assertTrue((AlertaLeida.getOrigen().getId(),AlertaLeida.getTema(), AlertaLeida.getContenido()) in map (lambda alert : (alert.getOrigen().getId(), alert.getTema(), alert.getContenido()),Cliente2.getBAL().getBuzon() ) )
         #Y que la leida sea igual a la que mando MESSI
         self.assertTrue((AlertaLeida.getOrigen().getId(),AlertaLeida.getTema(), AlertaLeida.getContenido()) == (Alerta1.getOrigen().getId(),Alerta1.getTema(), Alerta1.getContenido()))
    def test_Punto9(self):
        #creamos el Adm
        AdmEventos = Server.Servidor()
        ###Creamos Los buzones de cada Usuario
            #Buzon Messi
        B1M = Buzon.LIFO(msjs = [])
        B2M = Buzon.FIFO(msjs = [])
        B3M = Buzon.FIFO(msjs = [])
            #Buzon Diego
        B4M = Buzon.LIFO(msjs = [])
        B5M = Buzon.FIFO(msjs = [])
        B6M = Buzon.FIFO(msjs = [])
        #Creamos un usuario
        Cliente1 = Cliente.Cliente("Messi", 1, AdmEventos,B1M,B2M,B3M)
        Cliente2 = Cliente.Cliente("Maradona", 2, AdmEventos,B4M,B5M,B6M)
        
        Cliente1.clienteRegistrarmeConTodasSuscripcion()
        Cliente2.clienteRegistrarmeConTodasSuscripcion()
        
        #Registramos los temas
        Cliente1.clienteRegistrarNuevoTema("Motos")
        Cliente2.clienteRegistrarNuevoTema("Remera")
        
        #Solo Diego le va a interesar los autos
        Cliente2.clienteRegistarmeATema("Remera")
        
        #Todas las alertas sin vencer como las propuestas y un par vencida
        AlertaI1 = Alerta.Informativa("Remera","I1 Casaca Colon 2pe", Cliente1, 2023, 12, 24, 00, 00, 00, destino = Cliente2)
        AlertaI2 = Alerta.Informativa("Remera","I2 Remera F1 Casi Nueva 6000USD", Cliente1, 2023, 6, 1, 12, 24, 33)
        AlertaU1 = Alerta.Urgente("Remera", "U1 Remera del Potro 500p", Cliente1, 2023, 12, 1, 13, 25, 55)
        AlertaI3 = Alerta.Informativa("Remera", "I3 Remera de Shilton Mundial 86", Cliente1, 2023, 4, 20, 00, 00, 00)
        AlertaU2 = Alerta.Urgente("Remera", "U2 Remera Puma", Cliente1, 2023, 6, 27, 12, 6, 5, destino = Cliente2 )
        AlertaI4 = Alerta.Informativa("Remera", "I4 Remera Villareal", Cliente1, 2023, 5, 6, 7, 14, 00, destino = Cliente2)
        AlertaVencida = Alerta.Informativa("Remera", "VENCIDA", Cliente1, 2020, 5, 6, 7, 14, 00, destino = Cliente2)

        #Messi manda todassss
        Cliente1.clienteEnviarAlerta(AlertaI1)
        Cliente1.clienteEnviarAlerta(AlertaI2)
        Cliente1.clienteEnviarAlerta(AlertaU1)
        Cliente1.clienteEnviarAlerta(AlertaI3)
        Cliente1.clienteEnviarAlerta(AlertaU2)
        Cliente1.clienteEnviarAlerta(AlertaI4)
        Cliente1.clienteEnviarAlerta(AlertaVencida)
        
        AlertasPUNTO9 = Cliente2.obtenerAlertasNoExpiradasNoLeidas() 
        #No tiene que estar la alerta vencida
        self.assertTrue((AlertaVencida.getOrigen().getId(),AlertaVencida.getTema(), AlertaVencida.getContenido()) not in map (lambda alert : (alert.getOrigen().getId(), alert.getTema(), alert.getContenido()),AlertasPUNTO9 ) )
        
        #Verificamos el orden propuesto [U2,U1,I1,I2,I3,I4]
        U2 = AlertasPUNTO9.pop(0)
        self.assertTrue((U2.getOrigen().getId(),U2.getTema(), U2.getContenido()) == (AlertaU2.getOrigen().getId(),AlertaU2.getTema(), AlertaU2.getContenido()))

        U1 = AlertasPUNTO9.pop(0)
        self.assertTrue((U1.getOrigen().getId(),U1.getTema(), U1.getContenido()) == (AlertaU1.getOrigen().getId(),AlertaU1.getTema(), AlertaU1.getContenido()))
        
        I1 = AlertasPUNTO9.pop(0)
        self.assertTrue((I1.getOrigen().getId(),I1.getTema(), I1.getContenido()) == (AlertaI1.getOrigen().getId(),AlertaI1.getTema(), AlertaI1.getContenido()))
        
        I2 = AlertasPUNTO9.pop(0)
        self.assertTrue((I2.getOrigen().getId(),I2.getTema(), I2.getContenido()) == (AlertaI2.getOrigen().getId(),AlertaI2.getTema(), AlertaI2.getContenido()))
        
        I3 = AlertasPUNTO9.pop(0)
        self.assertTrue((I3.getOrigen().getId(),I3.getTema(), I3.getContenido()) == (AlertaI3.getOrigen().getId(),AlertaI3.getTema(), AlertaI3.getContenido()))
        
        I4 = AlertasPUNTO9.pop(0)
        self.assertTrue((I4.getOrigen().getId(),I4.getTema(), I4.getContenido()) == (AlertaI4.getOrigen().getId(),AlertaI4.getTema(), AlertaI4.getContenido()))

    def test_Punto10(self):
       #creamos el Adm
       AdmEventos = Server.Servidor()
       ###Creamos Los buzones de cada Usuario
           #Buzon Messi
       B1M = Buzon.LIFO(msjs = [])
       B2M = Buzon.FIFO(msjs = [])
       B3M = Buzon.FIFO(msjs = [])
           #Buzon Diego
       B4M = Buzon.LIFO(msjs = [])
       B5M = Buzon.FIFO(msjs = [])
       B6M = Buzon.FIFO(msjs = [])
       #Creamos un usuario
       Cliente1 = Cliente.Cliente("Messi", 1, AdmEventos,B1M,B2M,B3M)
       Cliente2 = Cliente.Cliente("Maradona", 2, AdmEventos,B4M,B5M,B6M)
       
       Cliente1.clienteRegistrarmeConTodasSuscripcion()
       Cliente2.clienteRegistrarmeConTodasSuscripcion()
       
       #Registramos los temas
       Cliente1.clienteRegistrarNuevoTema("Motos")
       Cliente2.clienteRegistrarNuevoTema("Remera")
       
       #Solo Diego le va a interesar los autos
       Cliente2.clienteRegistarmeATema("Remera")
       
       #Todas las alertas sin vencer como las propuestas y un par vencida
       AlertaI1 = Alerta.Informativa("Remera","I1 Casaca Colon 2pe", Cliente1, 2023, 12, 24, 00, 00, 00, destino = Cliente2)
       AlertaI2 = Alerta.Informativa("Remera","I2 Remera F1 Casi Nueva 6000USD", Cliente1, 2023, 6, 1, 12, 24, 33)
       AlertaU1 = Alerta.Urgente("Remera", "U1 Remera del Potro 500p", Cliente1, 2023, 12, 1, 13, 25, 55)
       AlertaI3 = Alerta.Informativa("Remera", "I3 Remera de Shilton Mundial 86", Cliente1, 2023, 4, 20, 00, 00, 00)
       AlertaU2 = Alerta.Urgente("Remera", "U2 Remera Puma", Cliente1, 2023, 6, 27, 12, 6, 5, destino = Cliente2 )
       AlertaI4 = Alerta.Informativa("Remera", "I4 Remera Villareal", Cliente1, 2023, 5, 6, 7, 14, 00, destino = Cliente2)
       AlertaVencida = Alerta.Informativa("Remera", "VENCIDA", Cliente1, 2020, 5, 6, 7, 14, 00, destino = Cliente2)
       AlertaOtroTema = Alerta.Urgente("Motos", "VENCIDA", Cliente1, 2024, 5, 6, 7, 14, 00, destino = Cliente2)

       #Messi manda todassss
       Cliente1.clienteEnviarAlerta(AlertaI1)
       Cliente1.clienteEnviarAlerta(AlertaI2)
       Cliente1.clienteEnviarAlerta(AlertaU1)
       Cliente1.clienteEnviarAlerta(AlertaI3)
       Cliente1.clienteEnviarAlerta(AlertaU2)
       Cliente1.clienteEnviarAlerta(AlertaI4)
       Cliente1.clienteEnviarAlerta(AlertaVencida)
       Cliente1.clienteEnviarAlerta(AlertaOtroTema)
       
       AlertasPUNTO10 = Cliente2.obtenerAlertasNoExpiradasTema("Remera") 
       #No tiene que estar la alerta vencida
       self.assertTrue((AlertaVencida.getOrigen().getId(),AlertaVencida.getTema(), AlertaVencida.getContenido()) not in map (lambda alert : (alert[0].getOrigen().getId(), alert[0].getTema(), alert[0].getContenido()),AlertasPUNTO10 ) )
       #No tiene que estar la alerta de tema motos aunque no expire
       self.assertTrue((AlertaOtroTema.getOrigen().getId(),AlertaOtroTema.getTema(), AlertaOtroTema.getContenido()) not in map (lambda alert : (alert[0].getOrigen().getId(), alert[0].getTema(), alert[0].getContenido()),AlertasPUNTO10 ) )
       
       #el cliente 2 lee un poco su buzon para complicar las cosas
           #Leo 3 de urgentes
       Cliente2.leer(buzon = 0)
       Cliente2.leer(buzon = 0)
       Cliente2.leer(buzon = 0)
           #Leo 2 de informativas
       Cliente2.leer(buzon = 1)
       Cliente2.leer(buzon = 1)
       
       
       #Verificamos el orden propuesto [U2,U1,I1,I2,I3,I4]
       #Recordamos que lo que devuelve es una lista de tuplas (alerta, str)
       U2 = AlertasPUNTO10.pop(0)
       self.assertTrue((U2[0].getOrigen().getId(),U2[0].getTema(), U2[0].getContenido()) == (AlertaU2.getOrigen().getId(),AlertaU2.getTema(), AlertaU2.getContenido()))

       U1 = AlertasPUNTO10.pop(0)
       self.assertTrue((U1[0].getOrigen().getId(),U1[0].getTema(), U1[0].getContenido()) == (AlertaU1.getOrigen().getId(),AlertaU1.getTema(), AlertaU1.getContenido()))
       
       I1 = AlertasPUNTO10.pop(0)
       self.assertTrue((I1[0].getOrigen().getId(),I1[0].getTema(), I1[0].getContenido()) == (AlertaI1.getOrigen().getId(),AlertaI1.getTema(), AlertaI1.getContenido()))
       
       I2 = AlertasPUNTO10.pop(0)
       self.assertTrue((I2[0].getOrigen().getId(),I2[0].getTema(), I2[0].getContenido()) == (AlertaI2.getOrigen().getId(),AlertaI2.getTema(), AlertaI2.getContenido()))
       
       I3 = AlertasPUNTO10.pop(0)
       self.assertTrue((I3[0].getOrigen().getId(),I3[0].getTema(), I3[0].getContenido()) == (AlertaI3.getOrigen().getId(),AlertaI3.getTema(), AlertaI3.getContenido()))
       
       I4 = AlertasPUNTO10.pop(0)
       self.assertTrue((I4[0].getOrigen().getId(),I4[0].getTema(), I4[0].getContenido()) == (AlertaI4.getOrigen().getId(),AlertaI4.getTema(), AlertaI4.getContenido()))

    """
SELECT DISTINCT Clientes.Nombre, Clientes.Apellido, Clientes.ID
FROM [Clientes]
LEFT JOIN Ventas ON Ventas.Id_cliente = Clientes.ID
WHERE Importe >= 100000 AND  OrderDate >= '2022-04-01' AND  '2023-04-01' >= OrderDate
    """
if __name__ == '__main__':
    unittest.main()