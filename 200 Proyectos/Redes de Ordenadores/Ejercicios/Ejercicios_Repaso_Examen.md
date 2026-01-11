# Hoja de Ejercicios de Repaso - Redes de Ordenadores

Generado para: Javier Liaño Rioz (Midas)

Objetivo: Preparación Examen Final (Simulación de Escenarios Reales y Tipo Examen)

---

## Bloque 1: Fundamentos de Redes

### Ejercicio 1: Encapsulamiento y Capas
**Enunciado**: Describa el proceso de encapsulamiento que sufre un mensaje de aplicación (HTTP) al descender por la pila TCP/IP. Indique qué información crítica añade cada capa.

### Ejercicio 2: OSI vs TCP/IP
**Enunciado**: ¿Por qué el modelo TCP/IP no incluye las capas de Sesión y Presentación del modelo OSI? ¿Dónde reside esa funcionalidad en el mundo real?

### Ejercicio 3: Retardos en la Red
**Enunciado**: Un paquete de 1500 bytes se envía a través de un enlace de 1 Mbps de 1000 km de longitud. La velocidad de propagación es $2 \cdot 10^8$ m/s. Calcule el retardo de transmisión y el retardo de propagación.

### Ejercicio 4: Tipos de Conmutación
**Enunciado**: Compare la conmutación de circuitos frente a la de paquetes en términos de reserva de recursos y comportamiento ante picos de tráfico.

---

## Bloque 2: Capa Física

### Ejercicio 5: Límite de Nyquist
**Enunciado**: Un canal de voz tiene un ancho de banda de 3100 Hz (de 300 Hz a 3400 Hz). Si se usa una señal de 8 niveles, ¿cuál es la tasa máxima teórica de bits según Nyquist?

### Ejercicio 6: Capacidad de Shannon
**Enunciado**: El canal anterior (`B = 3100 Hz`) tiene una relación Señal/Ruido (SNR) de 30 dB. ¿Cuál es su capacidad máxima real?

### Ejercicio 7: Atenuación en Fibra
**Enunciado**: Una fibra óptica tiene una pérdida de 0.5 dB/km. Si se introduce una señal de 100 mW y el receptor necesita al menos 1 mW para funcionar, ¿cuál es la distancia máxima del enlace?

### Ejercicio 8: Ventajas de la Señal Digital
**Enunciado**: Mencione dos ventajas de la transmisión digital frente a la analógica en presencia de ruido.

---

## Bloque 3: Enlace de Datos

### Ejercicio 9: Transmisión Transparente (Byte Stuffing)
**Enunciado**: Una trama usa el carácter `FLAG` (01111110) como delimitador. Si el cuerpo del mensaje contiene el dato `01111110`, ¿cómo evita la capa de enlace que el receptor lo confunda con el final de la trama?

### Ejercicio 10: Eficiencia de Parada y Espera
**Enunciado**: En un enlace de 1 Gbps con un RTT de 80 ms, enviamos tramas de 8000 bits usando Parada y Espera. Calcule la utilización del canal ($U$).

### Ejercicio 11: Go-Back-N vs Selective Repeat
**Enunciado**: Se pierden las tramas 2 y 5 en una ventana de tamaño 4 (tramas 0 a 7). ¿Qué tramas retransmite Go-Back-N y qué tramas Selective Repeat tras agotarse los temporizadores?

### Ejercicio 12: CRC Receptivo
**Enunciado**: El receptor recibe el mensaje `101101` y el polinomio generador es $P(X) = X^3+1$. ¿Es la trama correcta?

---

## Bloque 4: LAN y Acceso al Medio

### Ejercicio 13: CSMA/CD y Longitud de Trama
**Enunciado**: ¿Por qué existe una longitud mínima de trama en Ethernet (64 bytes)?

### Ejercicio 14: Dominios de Colisión y Difusión
**Enunciado**: Un switch de 8 puertos tiene conectados 4 Hubs. ¿Cuántos dominios de colisión y cuántos de difusión hay?

### Ejercicio 15: Algoritmo de Spanning Tree (STP)
**Enunciado**: ¿Cuál es el objetivo principal del protocolo STP en una red con switches redundantes?

### Ejercicio 16: VLAN Tagging (802.1Q)
**Enunciado**: Explique la diferencia entre un puerto de "Acceso" y un puerto "Trunk".

---

## Bloque 5: Interconexión de Redes (Capa de Red)

### Ejercicio 17: Fragmentación IP y Offset
**Enunciado**: Un datagrama de 2400 bytes (cabecera de 20 bytes incluida) llega a un router cuya interfaz de salida tiene una MTU de 1000 bytes. Calcule el tamaño de datos y el valor del campo *Fragment Offset* para el segundo fragmento.

### Ejercicio 18: Funcionamiento de ARP
**Enunciado**: El Host A (IP_A, MAC_A) quiere enviar un paquete al Host B (IP_B, MAC_B) en la misma red local. La tabla ARP de A está vacía. Describa los mensajes ARP que se intercambian.

### Ejercicio 19: Máscaras de Subred (CIDR)
**Enunciado**: Dada la dirección `172.16.10.50/28`, calcule: a) La máscara en formato decimal, b) La dirección de red y c) La dirección de broadcast.

### Ejercicio 20: ICMP y TTL
**Enunciado**: ¿Qué mensaje ICMP genera un router cuando recibe un paquete con `TTL = 1` y el destino no es él mismo? ¿Para qué sirve esto en la herramienta `traceroute`?

### Ejercicio 21: DHCP (Proceso DORA)
**Enunciado**: Nombre las cuatro fases del protocolo DHCP para que un cliente obtenga una dirección IP.

### Ejercicio 22: Algoritmos de Enrutamiento
**Enunciado**: ¿Cuál es la principal diferencia entre un protocolo de Vector de Distancias (ej. RIP) y uno de Estado de Enlace (ej. OSPF)?

---

## Bloque 6: Capa de Transporte

### Ejercicio 23: UDP y Fiabilidad
**Enunciado**: Si UDP no garantiza la entrega ni el orden, ¿por qué protocolos como DNS o el Streaming de vídeo lo prefieren frente a TCP?

### Ejercicio 24: Establecimiento de Conexión TCP
**Enunciado**: Dibuje o explique el intercambio de flags (SYN, ACK) en el "Three-Way Handshake" de TCP.

### Ejercicio 25: Ventana de Congestión (Slow Start)
**Enunciado**: Un emisor TCP comienza en fase de Slow Start con un `MSS = 1 KB` y su ventana inicial `cwnd = 1 KB`. Si no hay pérdidas, ¿qué tamaño tendrá la `cwnd` tras 3 RTTs?

### Ejercicio 26: Puertos y Sockets
**Enunciado**: ¿Puede un servidor Web (puerto 80) mantener abiertas simultáneamente conexiones con cientos de clientes distintos? Explique cómo los distingue.

---

## Bloque 7: Seguridad en Redes

### Ejercicio 27: Triada CIA
**Enunciado**: Un atacante intercepta un correo electrónico y lo lee sin permiso. ¿Qué pilar de la triada de seguridad se ha visto comprometido? ¿Y si lo modifica antes de que llegue?

### Ejercicio 28: Tipos de Firewall
**Enunciado**: Explique la diferencia entre un Firewall de Filtrado de Paquetes y uno de Inspección de Estado (Stateful).

### Ejercicio 29: Ataque de Denegación de Servicio (DoS)
**Enunciado**: ¿En qué consiste un ataque de SYN Flood?

### Ejercicio 30: Seguridad en Wi-Fi
**Enunciado**: ¿Por qué no se recomienda el uso del cifrado WEP hoy en día?

---

## 🟢 Bloque 1: Fundamentos y Medios de Transmisión (Temas 1 y 2)

**Objetivo:** Asegurar puntos fáciles sobre retardos y conceptos físicos.

1. **Cálculo de Retardos:** Imagina un enlace punto a punto de 50 km entre dos servidores. La velocidad de propagación en el medio es $2 \cdot 10^8$ m/s y el ancho de banda del enlace es de 1 Gbps. Queremos enviar un archivo de 500 MB.
    
    - a) Calcula el retardo de propagación.
        
    - b) Calcula el retardo de transmisión.
        
    - c) ¿Cuál de los dos es dominante? ¿Si aumentamos el ancho de banda a 10 Gbps, cuál sería el nuevo tiempo total (ignorando procesamiento y colas)?
        
2. **Codificación:** Si tenemos un canal con un ancho de banda de 4 kHz y utilizamos una señal con 8 niveles de tensión distintos para codificar los datos (sin ruido).
    
    - a) ¿Cuál es la velocidad de modulación (baudios) máxima teórica según Nyquist?
        
    - b) ¿Cuántos bits enviamos por símbolo?
        
    - c) ¿Cuál es la velocidad binaria (bps) máxima?
        
3. **Medios Guiados vs No Guiados:**
    
    - Explica técnicamente por qué la fibra óptica es inmune a las interferencias electromagnéticas (EMI) a diferencia del par trenzado de cobre.
        
    - En un cable UTP Cat 6, ¿para qué sirve el trenzado de los pares?
        
4. **Topologías:** Dibuja y explica brevemente la diferencia en tolerancia a fallos entre una topología en Bus, en Estrella y en Malla completa.
    
5. **Concepto de Protocolo:** Define qué es un protocolo en el contexto de redes y menciona las tres partes clave (Sintaxis, Semántica, Temporización).
    

## 🔵 Bloque 2: Capa de Enlace y Control de Flujo (Tema 3)

**Objetivo:** Dominar detección de errores y ventanas deslizantes (muy común en problemas).

6. **CRC (Código de Redundancia Cíclica):**
    
    - Mensaje original $M(x) = 110101$.
        
    - Polinomio generador $G(x) = 101$ ($x^2 + 1$).
        
    - Calcula la trama final que se envía por la red (Mensaje + FCS). _Recuerda hacer la división XOR._
        
7. **Hamming:**
    
    - Si queremos enviar el dato `1011` usando Código Hamming para corregir errores de 1 bit, ¿cuántos bits de paridad necesitamos y cuál sería la trama enviada (asumiendo paridad par)?
        
8. **Parada y Espera (Stop & Wait):**
    
    - Explica qué sucede si se pierde el ACK (confirmación) en un protocolo de Parada y Espera. ¿Cómo evita el emisor quedarse bloqueado infinitamente y cómo sabe el receptor que es una trama duplicada?
        
9. **Ventana Deslizante (Go-Back-N):**
    
    - Tenemos un protocolo Go-Back-N con tamaño de ventana $N=4$.
        
    - El emisor envía las tramas 0, 1, 2, 3.
        
    - La trama 1 se pierde. Las tramas 0, 2 y 3 llegan bien.
        
    - Describe la secuencia de ACKs que envía el receptor y qué tramas retransmite el emisor al vencer el temporizador.
        
10. **Eficiencia de Utilización:**
    
    - Tenemos un canal satelital con un RTT de 500 ms. La velocidad es 1 Mbps y el tamaño de trama es 1000 bits.
        
    - Calcula la eficiencia del uso del canal ($U$) si usamos Parada y Espera.
        
    - ¿Qué tamaño de ventana mínimo necesitaríamos en un protocolo de ventana deslizante para lograr una eficiencia cercana al 100%?
        

## 🟡 Bloque 3: LANs, Ethernet y Conmutación (Tema 4) - CRÍTICO

**Objetivo:** Este es el núcleo del examen práctico (basado en tus PDFs).

11. **CSMA/CD:**
    
    - Explica el algoritmo de _backoff_ exponencial binario que usa Ethernet cuando detecta una colisión. ¿Por qué aumenta el tiempo de espera aleatorio en cada reintento?
        
12. **Dominios de Colisión y Difusión:**
    
    - Tienes una red con 1 Router, 2 Switches y 1 Hub.
        
    - Dibuja un esquema simple conectándolos.
        
    - Rodea con un círculo rojo los dominios de colisión y con uno azul los dominios de difusión (broadcast).
        
13. **Direcciones MAC:**
    
    - ¿Qué es una dirección MAC de difusión (broadcast)? Escríbela en hexadecimal.
        
    - ¿Cómo diferencia un switch una trama Unicast de una Multicast mirando el primer byte de la MAC destino?
        
14. **VLANs:**
    
    - Explica el concepto de "Puerto Trunk" (o etiquetado 802.1Q) frente a un "Puerto de Acceso".
        
    - Si una trama sale de un puerto de acceso de la VLAN 10 hacia un PC, ¿lleva la etiqueta (tag) de la VLAN?
        
15. **STP (Spanning Tree Protocol):**
    
    - ¿Cuál es la función principal del protocolo STP en una red conmutada redundante? ¿Qué pasaría si desactivamos STP y conectamos dos cables entre dos switches?
        

## 🟠 Bloque 4: Capa de Red e IP (Tema 5)

**Objetivo:** Soltura con direcciones IP, subredes y fragmentación.

16. **Fragmentación IP:**
    
    - Un datagrama IP de 4000 bytes (20 cabecera + 3980 datos) debe atravesar una red con MTU = 1500 bytes.
        
    - Calcula cuántos fragmentos se generan.
        
    - Indica para cada fragmento: Tamaño total, Flag MF (More Fragments) y Offset.
        
17. **Clasificación IP:**
    
    - Dada la IP `172.16.50.4` con máscara `/19`.
        
    - Calcula: Dirección de Red, Dirección de Broadcast y Rango de IPs útiles para hosts.
        
18. **Subnetting (VLSM):**
    
    - La empresa "MidasDev" tiene la red `192.168.10.0/24`. Necesita crear subredes para los siguientes departamentos (optimiza el espacio):
        
        - Desarrollo: 60 hosts.
            
        - Marketing: 25 hosts.
            
        - Dirección: 10 hosts.
            
        - Enlaces WAN (x3): 2 IPs cada uno.
            
    - Asigna las subredes (Dirección de red y máscara) para cada caso.
        
19. **Tablas de Enrutamiento:**
    
    - Un router recibe un paquete con destino `10.1.1.75`. Su tabla de rutas es:
        
        - Ruta A: `10.1.1.0/24` vía Interfaz 1.
            
        - Ruta B: `10.1.1.64/26` vía Interfaz 2.
            
        - Ruta C: `0.0.0.0/0` vía Interfaz 3.
            
    - ¿Por qué interfaz saldrá el paquete? (Aplica el criterio de _Longest Prefix Match_).
        
20. **ICMP y ARP:**
    
    - ¿Para qué sirve el protocolo ARP? Describe el proceso cuando el PC A quiere enviar un ping al PC B (en la misma subred) y conoce su IP pero no su MAC.
        
    - ¿Qué mensaje ICMP se genera cuando un router descarta un paquete porque el TTL ha llegado a 0?
        

## 🔴 Bloque 5: Capa de Transporte (Tema 6)

**Objetivo:** Entender la "inteligencia" de la comunicación extremo a extremo.

21. **TCP vs UDP:**
    
    - Enumera 3 diferencias clave.
        
    - Indica qué protocolo usarías para: a) Streaming de video en vivo (Zoom), b) Descarga de un archivo .exe, c) Consultas DNS.
        
22. **Three-Way Handshake (TCP):**
    
    - Dibuja el diagrama de establecimiento de conexión TCP.
        
    - Incluye los flags (SYN, ACK) y números de secuencia iniciales ($x$, $y$) hipotéticos.
        
23. **Control de Congestión TCP:**
    
    - Explica las fases de "Arranque Lento" (Slow Start) y "Evitación de la Congestión" (Congestion Avoidance).
        
    - ¿Qué evento suele provocar que la ventana de congestión caiga drásticamente?
        
24. **Puertos:**
    
    - Si ejecutas un comando `netstat` y ves una conexión en estado `ESTABLISHED` con dirección local `192.168.1.50:54321` y remota `8.8.8.8:53`.
        
    - ¿Quién es el cliente y quién el servidor? ¿Qué protocolo de aplicación se está usando probablemente?
        
25. **Control de Flujo:**
    
    - ¿Qué campo de la cabecera TCP se utiliza para el control de flujo y qué le indica al emisor?
        

## ⚫ Bloque 6: Seguridad y General (Tema 7)

**Objetivo:** Conceptos básicos que suelen caer como preguntas teóricas.

26. **Confidencialidad, Integridad y Disponibilidad (CIA):**
    
    - Define brevemente cada uno.
        
    - ¿Qué ataque compromete la Disponibilidad? (Ej: DoS).
        
27. **Firewalls:**
    
    - Diferencia entre un Firewall de filtrado de paquetes (Stateless) y uno de inspección de estado (Stateful).
        
28. **DMZ (Zona Desmilitarizada):**
    
    - ¿Qué tipos de servidores se colocan habitualmente en una DMZ y por qué no se ponen en la red interna (LAN)?
        

## 🔥 Bloque 7: SIMULACRO TIPO EXAMEN (La prueba de fuego)

_Este ejercicio está diseñado basándome en el Ejercicio 1 del Examen Final 23/24 y el Parcial de este año. **Hazlo con calma, es el más importante.**_

### Ejercicio 29: Switching y VLANs (El "Clásico" del profesor)

**Escenario:**

- Tenemos la topología: **PC A** y **PC B** conectados al **Switch X**.
    
- **PC C** y **PC D** conectados al **Switch Y**.
    
- Los Switches **X** e **Y** están conectados entre sí por el puerto 24 de ambos.
    
- **VLANs:**
    
    - VLAN 10: PC A y PC C.
        
    - VLAN 20: PC B y PC D.
        
- **Configuración:**
    
    - Puertos hacia los PCs son modo "Acceso".
        
    - El enlace entre X e Y (puerto 24) es modo "Trunk" (permite VLAN 10 y 20).
        
- **Estado inicial:** Todas las tablas MAC están vacías.
    

**Secuencia de Eventos (Rellena la tabla):**

|   |   |   |   |   |
|---|---|---|---|---|
|**Evento #**|**Acción**|**Tabla MAC Switch X (Aprende)**|**Tabla MAC Switch Y (Aprende)**|**¿Por qué puertos se reenvía la trama? (Detalla si sale con Tag o sin Tag)**|
|**1**|A envía trama a C|MAC_A en puerto...||Switch X: ...<br><br>  <br><br>Switch Y: ...|
|**2**|C responde a A||MAC_C en puerto...|Switch Y: ...<br><br>  <br><br>Switch X: ...|
|**3**|B envía trama a A|MAC_B en puerto...||Switch X: ...|
|**4**|D envía trama a B||MAC_D en puerto...|Switch Y: ...<br><br>  <br><br>Switch X: ...|
|**5**|A envía trama de Broadcast|||Switch X: ...<br><br>  <br><br>Switch Y: ...|

**Preguntas extra sobre el ejercicio:**

- En el Evento 3, ¿Llega la trama a A? ¿Por qué?
    
- En el enlace troncal (puerto 24), ¿cómo se diferencia la trama del evento 1 de la trama del evento 4?
    

### Ejercicio 30: Direccionamiento Integral

La Universidad tiene asignado el bloque `200.10.10.0/24`. Se requiere diseñar la red para:

1. **Edificio A:** 100 equipos.
    
2. **Edificio B:** 50 equipos.
    
3. **Laboratorio:** 20 equipos.
    
4. **Wi-Fi Invitados:** Resto de IPs disponibles.
    

**Tarea:**

- Calcula la máscara, IP de red, IP de broadcast y primera/última IP útil para cada subred.
    
- Escribe la tabla de enrutamiento del Router Principal para llegar a estas subredes, asumiendo que cada una está conectada a una interfaz virtual (vlan 10, vlan 20, vlan 30, vlan 40).
    

### Ejercicio 31: Análisis de Tráfico (Wireshark teórico)

Se captura la siguiente trama hexadecimal (primeros bytes): `45 00 00 3C ...`

- **a)** Analizando el primer byte (`45`), ¿Qué versión de IP es y cuál es la longitud de la cabecera?
    
- **b)** Si el campo "Protocolo" dentro de la cabecera IP vale `06` (hex), ¿qué protocolo de transporte lleva dentro?
    
- **c)** Si el campo TTL vale `01`, ¿qué le pasará a este paquete al llegar al siguiente router?
    

## 💡 Consejos Finales para tu Examen

1. **Tablas de Switching:** El profesor evalúa si entiendes el **aprendizaje** (source MAC) vs el **reenvío** (destination MAC). Recuerda:
    
    - Un switch aprende mirando la MAC **Origen**.
        
    - Un switch decide por dónde sacar mirando la MAC **Destino**.
        
    - Si no conoce el destino -> _Flooding_ (inundación) por todos los puertos de esa VLAN (menos por el que entró).
        
    - **VLANs:** El tráfico de la VLAN 10 NUNCA pasa a la VLAN 20 a través de un switch L2. Necesitas un router. Si te preguntan si A (VLAN 10) puede hacer ping a B (VLAN 20) solo con switches L2, la respuesta es **NO**.
        
2. **Subnetting:** No falles en los bordes. Recuerda restar 2 IPs (red y broadcast) al calcular hosts útiles.
    
3. **Lectura:** En el examen del año pasado, había preguntas con "trampa" o detalles sutiles en el enunciado ("considere que las tablas están llenas" vs "tablas vacías"). Lee despacio.
    

---

*¡Ánimo Midas, dales duro! Si necesitas la solución detallada de alguno de estos ejercicios, pídela.*