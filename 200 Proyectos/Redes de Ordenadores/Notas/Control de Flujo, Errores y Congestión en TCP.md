# Control de Flujo, Errores y Congestión en TCP

TCP implementa mecanismos avanzados para garantizar la fiabilidad y eficiencia.

## Control de Flujo y Errores
- **Ventana Deslizante**: El receptor anuncia su espacio disponible en el campo **Window**. El emisor no puede enviar más allá de este límite.
- **Confirmación Acumulativa**: Un ACK confirma todos los bytes anteriores.
- **ARQ con Vuelta Atrás N**: Comportamiento por defecto ante pérdidas, aunque puede usar **SACK** (Selective ACK) si se negocia.
- **Fast Retransmit**: Si el emisor recibe 3 ACKs duplicados, retransmite el segmento perdido sin esperar al temporizador.

## Control de Congestión (No saturar la carretera)
- **Slow Start (Arranque Lento)**: Empiezas enviando 1, luego 2, luego 4, luego 8... duplicando hasta que detectas que la red se queja.
  - *Analogía*: Como entrar en una autopista. Empiezas despacio por el carril de aceleración y vas ganando velocidad según ves que hay hueco.
- **Congestion Avoidance**: Cuando ya vas rápido y estás cerca del límite, dejas de duplicar y solo sumas de uno en uno (+1) para no causar un choque.
- **Fast Retransmit**: Si recibes el mismo ACK tres veces seguidas, es que el otro está diciendo: "¡Me falta esto! ¡Me falta esto! ¡Me falta esto!". TCP no espera al tiempo de espera y lo envía ya.

---
**Relacionado**: [[Protocolo TCP - Servicio y Multiplexación]]
**Fuente**: [[62_Tema6.pdf]]
