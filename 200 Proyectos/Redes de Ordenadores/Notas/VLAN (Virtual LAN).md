# VLAN (Virtual LAN)

Agrupación lógica de terminales en un mismo dominio de difusión, independientemente de su ubicación física.

## Concepto y Beneficios
- **Analogía**: Tienes una oficina diáfana (un solo switch físico). Usas "paredes invisibles" (VLANs) para que el equipo de Contabilidad no vea lo que hace el de Marketing, aunque compartan el mismo techo y cables.
- **Trunk**: Un "pasillo" común por el que pueden pasar paquetes de todos los grupos, pero cada uno lleva su etiqueta para no mezclarse.

## Estándar IEEE 802.1Q
Cuando una trama pasa por un *Trunk*, se le añaden **4 bytes** extra a la cabecera Ethernet original:
- **VID (VLAN Identifier)**: 12 bits (identifica la VLAN, del 1 al 4094).
- **PCP (Priority Code Point)**: 3 bits (prioridad de la trama, usado en QoS).
- **DEI (Drop Eligible Indicator)**: 1 bit (indica si la trama puede tirarse en caso de congestión).

> [!CAUTION]
> Añadir estos 4 bytes cambia la trama, por lo que el **CRC (FCS)** debe recalcularse por completo en cada paso.

---
**Relacionado**: [[Dispositivos de Interconexión (Hubs vs Switches)]]
**Fuente**: [[42_Tema4.pdf]]
