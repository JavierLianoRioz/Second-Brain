# Principios de la Capa de Red

La capa de red (Capa 3) es responsable del transporte de paquetes extremo a extremo a través de múltiples saltos (routers).

## Funciones Principales
- **Enrutamiento (Routing)**: El "Cerebro". Decide el camino global.
  - *Analogía*: El sistema logístico de correos que decide que una carta de Madrid a Berlín debe pasar por París.
- **Reenvío (Forwarding)**: El "Brazo". Mueve el paquete de una entrada a una salida.
  - *Analogía*: El trabajador de correos que mira el código postal y mete la carta en la saca que va hacia París.

## Modelos de Red
- **Circuitos Virtuales**: Como una llamada telefónica fija; se reserva el camino antes de hablar.
- **Datagramas**: Como el correo postal. Cada carta (paquete) puede ir por una ruta distinta si el cartero ve que hay atasco en una calle.

---
**Relacionado**: [[Conceptos de Enrutamiento]], [[Protocolo IP (IPv4 e IPv6)]]
**Fuente**: [[52_Tema5.pdf]]
