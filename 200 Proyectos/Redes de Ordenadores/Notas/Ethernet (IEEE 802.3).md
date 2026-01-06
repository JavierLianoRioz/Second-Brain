# Ethernet (IEEE 802.3)

Ethernet es el estándar más extendido para redes LAN cableadas.

## Arquitectura IEEE 802
Divide la capa de enlace en:
- **LLC (Logical Link Control)**: Interfaz con capas superiores, común a todas las redes (802.2).
- **MAC (Media Access Control)**: Específica de cada tecnología (802.3 para Ethernet, 802.11 para WiFi). Gestiona el direccionamiento físico y el acceso al medio.
  - *Función Clave*: Permite la **entrega local**. Los dispositivos de capa 2 (Switches) usan la tabla de direcciones MAC para enviar la trama solo al puerto donde está el destinatario, en lugar de inundar toda la red.

## Direccionamiento MAC
- **Formato**: 48 bits (6 bytes) en hexadecimal.
- **OUI**: Los primeros 24 bits identifican al fabricante.
- **Tipos de Direcciones**:
  - **Unicast**: Un único destino.
  - **Multicast**: Grupo de destinos (primer byte impar).
  - **Broadcast**: Todos los nodos (`FF:FF:FF:FF:FF:FF`).

## Trama Ethernet
Existen dos formatos que coexisten (se distinguen por el valor del campo central):
- **Ethernet II (DIX)**: Campo central $\geq 1536$ (indica **Ethertype**, ej. `0x0800` para IP). Es la más común hoy.
- **IEEE 802.3**: Campo central $< 1536$ (indica **Longitud** de los datos).

**Campos comunes**:
- Direcciones (6B Destino + 6B Origen).
- Datos (46 a 1500 bytes).
- FCS (4B de CRC).

> [!NOTE]
> **Interframe Gap**: Se dejan 12 bytes de "silencio" entre tramas para que el receptor se recupere.

---
**Relacionado**: [[Dispositivos de Interconexión (Hubs vs Switches)]]
**Fuente**: [[42_Tema4.pdf]]
