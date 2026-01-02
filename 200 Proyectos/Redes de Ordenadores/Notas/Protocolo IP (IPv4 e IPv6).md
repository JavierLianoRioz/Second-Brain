# Protocolo IP (IPv4 e IPv6)

El Protocolo de Internet (IP) es el pilar de la capa de red en el modelo TCP/IP.

## Características de IP
- **Sin conexión**: No saluda antes de enviar (como tirar una carta al buzón).
- **Mejor esfuerzo (Best Effort)**: IP intenta que llegue, pero si hay problemas, tira el paquete a la basura y no avisa. La fiabilidad es cosa de capas superiores (TCP).
- **TTL (Time to Live)**: Un contador que baja en cada salto.
  - *Analogía*: Una "bomba de tiempo" en el paquete. Si el contador llega a 0 sin haber llegado al destino, el paquete se destruye para que no de vueltas infinitas por la red.

## IPv6 (128 bits)
- Diseñado para solventar el agotamiento de direcciones.
- Notación hexadecimal (ej. `2001:db8::1`).
- Elimina la necesidad de NAT gracias a su inmenso espacio de direcciones.
- Solo fragmenta el host origen (no los routers).

---
**Relacionado**: [[Direccionamiento IP y Subredes]], [[Fragmentación y NAT]]
**Fuente**: [[52_Tema5.pdf]]
