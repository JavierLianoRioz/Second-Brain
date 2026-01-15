# Control de Flujo, Errores y Congestión en TCP

TCP implementa mecanismos avanzados para garantizar la fiabilidad y eficiencia.

## Control de Flujo y Errores
- **Ventana Deslizante**: El receptor anuncia su espacio disponible en el campo **Window**. El emisor no puede enviar más allá de este límite.
- **Confirmación Acumulativa**: Un ACK confirma todos los bytes anteriores.
- **ARQ con Vuelta Atrás N**: Comportamiento por defecto ante pérdidas, aunque puede usar **SACK** (Selective ACK) si se negocia.
- **Fast Retransmit**: Si el emisor recibe 3 ACKs duplicados, retransmite el segmento perdido sin esperar al temporizador.

## Fórmula de Rendimiento (Throughput)
Para calcular a qué velocidad máxima puede transmitir TCP según su ventana ($W$) y el retardo ($RTT$):
- **$R = (W \times 8) / RTT$**
  - *Unidades*: Si $W$ está en bytes y $RTT$ en segundos, el resultado es en **bps** (bits por segundo).
  - *Nota*: En redes de satélite (alto $RTT$), necesitas una ventana $W$ enorme para que la velocidad no caiga.

## La Gran Mentira del Go-Back N
> [!CAUTION]
> Aunque las diapositivas teóricas suelen decir que TCP usa "ARQ con vuelta atrás N", en la realidad **TCP SÍ guarda los segmentos fuera de orden** (buffering) si tiene memoria.
> - **Examen**: Si te preguntan el modelo teórico del curso, di **Go-Back N**.
> - **Realidad/Ejercicios**: Si te preguntan por reordenación, recuerda que TCP es más listo y solo pide lo que falta (Selective ACK/Reject).

## Eficiencia en el Envío
- **Algoritmo de Nagle**: Para no enviar muchos paquetes diminutos (ej. de 1 byte), TCP espera un poco para agrupar varios caracteres en un solo segmento grande.
- **ACKs Retardados**: El receptor no contesta inmediatamente a cada mensaje; espera un instante por si tiene datos que enviar él también y así mete el "Gracias" (ACK) dentro de su mensaje de respuesta (**Piggybacking**).

## Control de Congestión (No saturar la carretera)
- **Slow Start (Arranque Lento)**: Empiezas enviando 1, luego 2, luego 4, luego 8... duplicando hasta que detectas que la red se queja.
  - *Analogía*: Como entrar en una autopista. Empiezas despacio por el carril de aceleración y vas ganando velocidad según ves que hay hueco.
  - **Umbral**: Cuando llegas a un límite previsto, pasas de duplicar a subir de uno en uno (+1) (**Congestion Avoidance**).
- **Fast Retransmit**: Si recibes el mismo ACK tres veces seguidas, es que el otro está diciendo: "¡Me falta esto! ¡Me falta esto! ¡Me falta esto!". TCP no espera al tiempo de espera y lo envía ya.

---
**Relacionado**: [Protocolo TCP - Servicio y Multiplexación](Protocolo%20TCP%20-%20Servicio%20y%20Multiplexaci%C3%B3n.md)
**Fuente**: [[62_Tema6.pdf]]
