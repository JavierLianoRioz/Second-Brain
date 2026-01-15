# Taxonomía de Redes

Las redes de ordenadores se pueden clasificar según diversos criterios: su área de distribución, la tecnología de transmisión o la técnica de conmutación.

## Clasificación por Área de Distribución
- **PAN (Personal Area Network)**: Uso personal (ej. Bluetooth entre móvil y reloj).
- **LAN (Local Area Network)**: Edificio o casa (ej. WiFi doméstico, Ethernet oficina).
- **CAN (Campus Area Network)**: Conjunto de edificios (ej. Universidad).
- **MAN (Metropolitan Area Network)**: Ciudad.
- **WAN (Wide Area Network)**: Extensa, países o continentes.

## Clasificación por Tecnología de Transmisión
- **Punto a Punto (Point-to-Point)**: Conexión directa única entre dos nodos.
  - **Simplex**: Transmisión en un solo sentido.
    - *Analogía*: Una calle de sentido único o la televisión tradicional.
  - **Half-duplex**: Ambos sentidos, pero no a la vez.
    - *Analogía*: Un Walkie-talkie o un puente estrecho de un solo carril.
  - **Full-duplex**: Ambos sentidos de forma simultánea.
    - *Analogía*: Una conversación telefónica o una autopista de varios carriles.
- **Difusión (Broadcast)**: El canal es compartido por todos los nodos.
  - **Unicast**: Envío de uno a uno (ej. Mensaje privado).
  - **Multicast**: Envío de uno a un grupo (ej. Grupo de WhatsApp).
  - **Broadcast**: Envío de uno a todos (ej. Grito en una habitación).

## Clasificación por Técnica de Conmutación
- **Conmutación de Circuitos**: Se reserva un camino físico dedicado.
  - *Analogía*: Reservar una mesa en un restaurante. El espacio es tuyo aunque no estés comiendo.
- **Conmutación de Paquetes**: Los datos se dividen en paquetes independientes.
  - *Analogía*: Pedir comida a domicilio. El repartidor usa las calles comunes y no necesita que la carretera esté reservada para él.

## Topologías Físicas
Modelan cómo están conectados los dispositivos físicamente:
- **Bus**: Todos los nodos en un mismo cable.
- **Estrella (Star)**: Un nodo central (Hub/Switch) conecta a todos.
- **Árbol (Tree)**: Jerarquía de estrellas.
- **Anillo (Ring)**: Conexión circular.
- **Malla (Mesh)**: Múltiples conexiones entre nodos (redundancia).

---
**Relacionado**: [Modelo General de Comunicaciones](Modelo%20General%20de%20Comunicaciones.md), [Arquitectura de Protocolos](Arquitectura%20de%20Protocolos.md)
**Fuente**: [[12_Tema1.pdf]]
