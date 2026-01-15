# Protocolo IP (IPv4 e IPv6)

El Protocolo de Internet (IP) es el pilar de la capa de red en el modelo TCP/IP.

## Características de IP
- **Sin conexión**: No saluda antes de enviar (como tirar una carta al buzón).
- **Mejor esfuerzo (Best Effort)**: IP intenta que llegue, pero si hay problemas, tira el paquete a la basura y no avisa. La fiabilidad es cosa de capas superiores (TCP).
- **TTL (Time to Live)**: Un contador que baja en cada salto.
  - *Analogía*: Una "bomba de tiempo" en el paquete. Si el contador llega a 0 sin haber llegado al destino, el paquete se destruye para que no de vueltas infinitas por la red.

## IPv4 (32 bits)
- **Cabecera**: Tiene un tamaño mínimo de **20 bytes** (sin opciones). Puede crecer hasta 60 bytes si incluye opciones.
- **IHL (Internet Header Length)**: Campo de 4 bits que indica el tamaño de la cabecera en palabras de 32 bits (mínimo 5).

## IPv6 (128 bits)
- Diseñado para solventar el agotamiento de direcciones.
- Notación hexadecimal (ej. `2001:db8::1`).
- Elimina la necesidad de NAT gracias a su inmenso espacio de direcciones.
- **Fragmentación en el Host Origen**: A diferencia de IPv4, los routers IPv6 **no** fragmentan los paquetes. Solo el emisor puede hacerlo.
  - *¿Por qué?*: Para que los routers sean mucho más rápidos. No pierden tiempo recortando y pegando "piezas" de datos.
  - *Analogía*: En IPv4, el cartero (Router) lleva unas tijeras y si el paquete no cabe por la ranura, lo corta en dos y lo envía. En IPv6, el cartero simplemente te devuelve el paquete (ICMPv6 Packet Too Big) y te dice: "Oye, hazlo más pequeño tú, que yo tengo prisa".
  - *Path MTU Discovery*: El host origen averigua el tamaño máximo permitido en todo el camino antes de enviar.

---
**Relacionado**: [Direccionamiento IP y Subredes](Direccionamiento%20IP%20y%20Subredes.md), [Fragmentación y NAT](Fragmentaci%C3%B3n%20y%20NAT.md)
**Fuente**: [[52_Tema5.pdf]]
