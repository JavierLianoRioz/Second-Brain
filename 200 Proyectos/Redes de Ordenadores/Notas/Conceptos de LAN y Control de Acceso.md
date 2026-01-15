# Conceptos de LAN y Control de Acceso

Una **LAN (Local Area Network)** es una red de alcance limitado (edificio) gestionada por una única entidad.

## Tipos de LAN
- **Medio Compartido**: Un único canal para todos.
  - *Analogía*: Una habitación donde todos gritan a la vez. Si dos hablan, nadie se entera de nada (colisión).
- **LAN Conmutada**: Uso de **Switches**.
  - *Analogía*: Un sistema de telefonía privada. Tú hablas directamente con quien quieres y nadie más estorba.

## Rendimiento en el Enlace
Para entender qué tan eficiente es un protocolo (como Stop & Wait), usamos el parámetro **$a$**:
- **$a = \text{B} / \text{L}$** (Capacidad del enlace en tramas).
- **$a < 1$**: Las tramas llegan al receptor antes de que el emisor termine de enviarlas (enlaces cortos/lentos).
- **$a > 1$**: Varias tramas pueden estar "en vuelo" simultáneamente (enlaces largos/rápidos, como satélites).

## Control de Acceso al Medio (MAC)
- **Centralizado**: Un "árbitro" da el turno de palabra.
- **Distribuido**: Los propios nodos se ponen de acuerdo.
  - *Analogía*: Una cena de amigos donde se espera a que el otro termine para hablar (o se interrumpe y se pide perdón).

---
**Relacionado**: [Protocolos de Acceso Múltiple (ALOHA y CSMA)](Protocolos%20de%20Acceso%20M%C3%BAltiple%20%28ALOHA%20y%20CSMA%29.md), [Dispositivos de Interconexión (Hubs vs Switches)](Dispositivos%20de%20Interconexi%C3%B3n%20%28Hubs%20vs%20Switches%29.md)
**Fuente**: [[42_Tema4.pdf]]
