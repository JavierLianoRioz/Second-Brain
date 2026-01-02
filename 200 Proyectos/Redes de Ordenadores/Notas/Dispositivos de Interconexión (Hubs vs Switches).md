# Dispositivos de Interconexión (Hubs vs Switches)

Evolución de los dispositivos para conectar equipos en una LAN.

## Hub (Concentrador) - Capa 1
- **Analogía**: Un megáfono. Lo que entra por un puerto sale gritado por todos los demás. Todos oyen todo, lo que es inseguro e ineficiente.
- **Dominio de Colisión**: Uno solo. Si dos equipos gritan al megáfono a la vez, el sonido se mezcla.

## Switch (Conmutador) - Capa 2
- **Analogía**: Un recepcionista inteligente. Sabe en qué oficina está cada persona. Si B envía una nota a E, el switch solo se la entrega a E. Nadie más se entera.
- **Dominio de Colisión**: Uno por cada cable. Dos parejas pueden hablar a la vez en cables distintos sin molestarse.
- **Funciones**:
  1. **Aprendizaje**: Registra la MAC de origen y el puerto en una tabla dinámica.
  2. **Retransmisión**: Envía la trama por el puerto correcto o inunda (**Flooding**) si la MAC es desconocida.
  3. **Evitación de Bucles**: Protocolo **Spanning Tree (STP)** para evitar tormentas de broadcast.

---
**Relacionado**: [[VLAN (Virtual LAN)]]
**Fuente**: [[42_Tema4.pdf]]
