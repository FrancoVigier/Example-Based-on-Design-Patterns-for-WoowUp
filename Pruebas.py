# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 14:31:11 2023

@author: usuario
"""

import Cliente
import Server
import Alerta
import Buzon
#Basado en el estilo arquitectonico de II, Implicit Invocation.
#Es bastante elastico el sistema announce-suscribe de los eventos
#dando bastante margen para poder restringir eventos a usuarios de forma
#estatica o dinamica, le podemos cargar ya las listas de suscritos a los eventos
#al Adm de antemano, etc. Lo bueno es que lo usuarios entre si nunca van a interacionar
# ni saben de la existencia de otros, la relacion la regula el AdmEventos.
# Si ponemos por ejemplo la lista de usuario posibles a registrarse, y ponemos privativo = 1
# en la suscripcionNewUser entonces si no estas en la lista de permitidos no entras
# pero como somos buenos el privativo = 0, todo mundo entra :)
if __name__ == "__main__":
    #creamos el Adm
    AdmEventos = Server.Servidor()
    
   # AdmEventos.SuscripcionOperaciones['Registrarse'].append(10)
   # AdmEventos.SuscripcionOperaciones['Registrarse'].append(20)
   # print(AdmEventos.SuscripcionOperaciones)
    
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
        #Buzon Ayala
    B10M = Buzon.LIFO(msjs = [])
    B11M = Buzon.FIFO(msjs = [])
    B12M = Buzon.FIFO(msjs = [])
        #Buzon Aimar
    B13M = Buzon.LIFO(msjs = [])
    B14M = Buzon.FIFO(msjs = [])
    B15M = Buzon.FIFO(msjs = [])
        
    
   
    #Creamos un usuario
    
    Cliente1 = Cliente.Cliente("Messi", 1, AdmEventos,B1M,B2M,B3M)
    Cliente2 = Cliente.Cliente("Maradona", 2, AdmEventos,B4M,B5M,B6M)
    Cliente3 = Cliente.Cliente("Riquelme", 3, AdmEventos,B7M,B8M,B9M)
    Cliente4 = Cliente.Cliente("Ayala", 4, AdmEventos,B10M,B11M,B12M)
    Cliente5 = Cliente.Cliente("Aimar", 5, AdmEventos,B13M,B14M,B15M)
    
    #Suscribimos a los usuarios a los eventos que queremos individualmente o 
    #a todos los eventos por Default. Solo basta con llamar al suscribe del 
    #Evento que queremos y que el Cliente ya esté registrado
    
    #AdmEventos.suscribirClienteATodoEvento(Cliente1) Forma estatica de declarar en el SV
    Cliente1.clienteRegistrarmeConTodasSuscripcion()
    
    #AdmEventos.suscribirClienteATodoEvento(Cliente2)
    Cliente2.clienteRegistrarmeConTodasSuscripcion()
    
    #AdmEventos.suscribirClienteATodoEvento(Cliente3)
    Cliente3.clienteRegistrarmeConTodasSuscripcion()
    
    #AdmEventos.suscribirClienteATodoEvento(Cliente4)
    Cliente4.clienteRegistrarmeConTodasSuscripcion()
    
    #AdmEventos.suscribirClienteATodoEvento(Cliente5)
    Cliente5.clienteRegistrarmeConTodasSuscripcion()
    #print(AdmEventos.SuscripcionOperaciones)
    #movStr = '\n'.join(map(str, AdmEventos.RegUsers))
    #print(movStr)
    
    #Creamos Las Alertas que Van a mandar los Users
        #Las alertas que va a mandar messi
    Alerta1 = Alerta.Urgente("Motos","Zanela 90cc 2pe", Cliente1, 2023, 12, 24, 00, 00, 00, destino = Cliente2)
    Alerta2 = Alerta.Urgente("Autos","Citroen Berlingo Casi Nueva 6000USD", Cliente1, 2023, 6, 1, 12, 24, 33)
    #print(Alerta1)
    #print(Alerta2)
        #Las alertas que va a mandar el diego
    Alerta3 = Alerta.Informativa("Cuarteto", "Disco del Potro 500p", Cliente2, 2022, 12, 1, 13, 25, 55)
    Alerta4 = Alerta.Informativa("Remera", "Remera de Shilton Mundial 86", Cliente2, 2023, 4, 20, 00, 00, 00)
    #print(Alerta3)
    #print(Alerta4)
        #Las alertas que va a mandar riquelme
    Alerta5 = Alerta.Urgente("Botines", "Botines Puma", Cliente3, 2023, 2, 27, 12, 6, 5, destino = Cliente5 )
    Alerta6 = Alerta.Urgente("Remera", "Remera Villareal", Cliente3, 2023, 5, 6, 7, 14, 00, destino = Cliente5)
    #print(Alerta5)
    #print(Alerta6)
        #Las alertas que va a mandar ayala
    Alerta7 = Alerta.Urgente("Autos", "Fiat 600", Cliente4, 2024, 2, 27, 12, 6, 5 )
    Alerta8 = Alerta.Urgente("Motos", "Yamaha 1200cc", Cliente4, 2022, 5, 6, 7, 14, 00)
    #print(Alerta7)
    #print(Alerta8)
        #Las alertas que va a mandar aimar
    Alerta9 = Alerta.Informativa("Pelotas", "Adidas Tango", Cliente5, 2023, 1, 1, 1, 1, 1 )
    Alerta10 = Alerta.Informativa("Pelotas", "Adidas Jabulani", Cliente5, 2024, 5, 6, 7, 14, 00, destino = Cliente1)
    #print(Alerta9)
    #print(Alerta10)
    
    #print(AdmEventos)

    #Cada User registra sus temas
    Cliente1.clienteRegistrarNuevoTema("Motos")
    Cliente1.clienteRegistrarNuevoTema("Autos")
    Cliente2.clienteRegistrarNuevoTema("Cuarteto")
    Cliente2.clienteRegistrarNuevoTema("Remera")
    Cliente3.clienteRegistrarNuevoTema("Botines")
    Cliente5.clienteRegistrarNuevoTema("Pelotas")
    #print(AdmEventos)
    
    #El Diego pide la lista de temas
    ListaDeTemasRegistrados = Cliente2.clienteObtenerListaDeTemas()
    print(ListaDeTemasRegistrados)
    
    #ElMomento: Las suscripciones a los temas
        #A messi le importa las Pelota, Botines y los Autos
    Cliente1.clienteRegistarmeATema("Pelotas")
    Cliente1.clienteRegistarmeATema("Botines")
    Cliente1.clienteRegistarmeATema("Autos")
    #print(AdmEventos)
        #A Diego solo le gustan las motos
    Cliente2.clienteRegistarmeATema("Motos")
        #A Riquelme le importan las remeras y pelotas
    Cliente3.clienteRegistarmeATema("Remera")
    Cliente3.clienteRegistarmeATema("Pelotas")
        #A ayala solo le importa el cuarteto
    Cliente4.clienteRegistarmeATema("Cuarteto")
        #A aimar le gusta todos los temas
    Cliente5.clienteRegistarmeATema("", allTopics = 1)
    #print(AdmEventos)
    
    #Cada Cliente manda sus alertas
    #_______________________________________________    
    #Messi Manda de Motos
    Cliente1.clienteEnviarAlerta(Alerta1)
    #Diego lo tiene la alerta en urgente
    #print(Cliente2)
    #Aimar no la tiene porque la alerta era p2p
    #print(Cliente5)
        #Messi manda Autos
    Cliente1.clienteEnviarAlerta(Alerta2)
        #Solo a Messi y aimar le gustan los autos
    #print(Cliente1)
    #print(Cliente5) #Ahora si aimar tiene la alerta porque fue un BROADCAST a los suscriptos al tema
    #_______________________________________________    
    #Diego tira su alerta de cuartetooooo, son ambas broadcast
    Cliente2.clienteEnviarAlerta(Alerta3)
    #print(Cliente4) #Ayala cuartetero
    #print(Cliente5) #Aimar le entra a todo
    #Diego Remera
    Cliente2.clienteEnviarAlerta(Alerta4)
    #print(Cliente3) #A riquelme le guta
    #print(Cliente5) #A Ayala too
    #_______________________________________________
    #Apuro las cosas para los demas...
    #Riquelme manda alerta
    Cliente3.clienteEnviarAlerta(Alerta5)
    Cliente3.clienteEnviarAlerta(Alerta6)
    #Ayala manda alertas
    Cliente4.clienteEnviarAlerta(Alerta7)
    Cliente4.clienteEnviarAlerta(Alerta8)
    #Aimar manda alertas
    Cliente5.clienteEnviarAlerta(Alerta9)
    Cliente5.clienteEnviarAlerta(Alerta10)
    #________________________________________________

    
    #Todas las alerta no expiradas NO LEIDAS. Punto 9
    AlertasMessi = Cliente1.obtenerAlertasNoExpiradasNoLeidas()
    #movStr1 = '\n'.join(map(str, AlertasMessi))
    #print(movStr1)
    
    AlertasAimar = Cliente5.obtenerAlertasNoExpiradasNoLeidas()
    movStr2 = '\n'.join(map(str, AlertasAimar))
    #print(movStr2)
    
    
    #print(Cliente5)
    #________________________________________________
    #Todas las alerta no expiradas LEIDAS Y NO LEIDAS Sobre un TEMA. Punto 10
    Cliente5.leer(buzon = 1)
    Cliente5.leer(buzon = 1)
    Cliente5.leer(buzon = 1)
    Cliente5.leer(buzon = 1)
    #AlertasAimar2 = Cliente5.obtenerAlertasNoExpiradasLeidas("Autos")
    #movStr3 = '\n'.join(map((lambda t: "("+str(t[0])+" , "+t[1]+")\n"), AlertasAimar2))
    #print(movStr3)

    #Alertas extra para testear el orden del 9 y 10
    #I1,I2,U1,I3,U2,I4
    B16M = Buzon.LIFO(msjs = [])
    B17M = Buzon.FIFO(msjs = [])
    B18M = Buzon.FIFO(msjs = [])
    Cliente6 = Cliente.Cliente("YO", 6, AdmEventos,B16M,B17M,B18M)
    Cliente6.clienteRegistrarmeConTodasSuscripcion()
    Cliente6.clienteRegistarmeATema("", allTopics = 1)
    #Todas las alertas sin vencer
    AlertaI1 = Alerta.Informativa("Remera","I1 Casaca Colon 2pe", Cliente1, 2023, 12, 24, 00, 00, 00, destino = Cliente6)
    AlertaI2 = Alerta.Informativa("Remera","I2 Remera F1 Casi Nueva 6000USD", Cliente1, 2023, 6, 1, 12, 24, 33)
    AlertaU1 = Alerta.Urgente("Remera", "U1 Remera del Potro 500p", Cliente2, 2023, 12, 1, 13, 25, 55)
    AlertaI3 = Alerta.Informativa("Remera", "I3 Remera de Shilton Mundial 86", Cliente2, 2023, 4, 20, 00, 00, 00)
    AlertaU2 = Alerta.Urgente("Remera", "U2 Remera Puma", Cliente3, 2023, 6, 27, 12, 6, 5, destino = Cliente6 )
    AlertaI4 = Alerta.Informativa("Remera", "I4 Remera Villareal", Cliente3, 2023, 5, 6, 7, 14, 00, destino = Cliente6)
 
    Cliente1.clienteEnviarAlerta(AlertaI1)
    Cliente1.clienteEnviarAlerta(AlertaI2)
    Cliente2.clienteEnviarAlerta(AlertaU1)
    Cliente2.clienteEnviarAlerta(AlertaI3)
    Cliente3.clienteEnviarAlerta(AlertaU2)
    Cliente3.clienteEnviarAlerta(AlertaI4)
    
    #print(Cliente6) #OK
    
    #punto 9
    AlertasYO = Cliente6.obtenerAlertasNoExpiradasNoLeidas() 
    movStr6 = '\n'.join(map(str, AlertasYO))
    #print(movStr6) #U2,U1,I1,I2,I3,I4
    
    AlertasYO2 = Cliente6.obtenerAlertasNoExpiradasNoLeidas() 
    movStr7 = '\n'.join(map(str, AlertasYO2))
    #print(movStr7) #U2,U1,I1,I2,I3,I4
    
    
    #punto10 #OK
    AlertasYO3 = Cliente6.obtenerAlertasNoExpiradasTema("Remera")
    movStr8 = '\n'.join(map((lambda t: "("+ str(t[0]) +" , "+ t[1] +")\n"), AlertasYO3))
    print(movStr8)
    """
    AlertasYO4 = Cliente6.obtenerAlertasNoExpiradasTema("Remera")
    movStr9 = '\n'.join(map((lambda t: "("+ str(t[0]) +" , "+ t[1] +")\n"), AlertasYO4))
    print(movStr9)
    """

   
    
    
    