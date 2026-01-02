# Ethernet (IEEE 802.3)

Ethernet es el estándar más extendido para redes LAN cableadas.

## Arquitectura IEEE 802
Divide la capa de enlace en:
- **LLC (Logical Link Control)**: Interfaz con capas superiores, común a todas las redes (802.2).
- **MAC (Media Access Control)**: Específica de cada tecnología (802.3 para Ethernet, 802.11 para WiFi). Gestiona el direccionamiento físico y el acceso al medio.

## Direccionamiento MAC
- **Formato**: 48 bits (6 bytes) en hexadecimal.
- **OUI**: Los primeros 24 bits identifican al fabricante.
- **Tipos de Direcciones**:
  - **Unicast**: Un único destino.
  - **Multicast**: Grupo de destinos (primer byte impar).
  - **Broadcast**: Todos los nodos (`FF:FF:FF:FF:FF:FF`).

## Trama Ethernet
Contiene: Dirección Destino, Dirección Origen, Tipo/Longitud, Datos (46-1500 bytes) y **FCS (CRC de 32 bits)**.

---
**Relacionado**: [[Dispositivos de Interconexión (Hubs vs Switches)]]
**Fuente**: [[42_Tema4.pdf]]
