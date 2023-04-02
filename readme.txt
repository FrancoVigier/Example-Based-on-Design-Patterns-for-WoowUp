Ejemplo Basado en Patrones de Diseño para WoowUp:
	Basado en el estilo arquitectónico de II (invocacion implicita) con 2 TADS: Cliente y Server
Propósito
Dos de las desventajas del DOO son:
	1. Para que un objeto pueda invocar los servicios de otro objeto el primero debe tener una
referencia a este último.
	2. Respecto del invocante, los servicios ofrecidos por un objeto están fijos en tiempo de compilación.
El estilo de Invocación Implícita (II) elimina estas dos desventajas cambiando el conector del
DOO (llamada a procedimiento) por el conector evento. Por lo tanto, el propósito de este estilo es
permitir a los objetos invocar servicios de otros objetos sin necesidad de conocer sus identidades y
permitir que, para los clientes de un objeto, las subrutinas en su interfaz no queden fijas en tiempo
de compilación

Modelo Computacional Subyacente
En el caso de que se piense en un administrador de eventos, el modelo computacional subyacente es el siguiente:
	Cada TAD y toolie suscribe, ante el administrador de eventos, uno o más de los procedimientos en su interfaz para uno o más eventos.
	Cuando un TAD o toolie anuncia un evento, el administrador de eventos lo recibe y lo distribuye a todos los suscriptores de ese evento.
	El administrador de eventos instrumenta la distribución de eventos haciendo llamadas a procedimiento a las subrutinas suscritas para cada evento.

Generalmente el ADM es una var global o se puede guardar en los clientes y solo que estos usen la INTERFAZ DE ANUNCIOS UNICAMENTE del ADM.
Generalmente se una en sist  distribuidos
