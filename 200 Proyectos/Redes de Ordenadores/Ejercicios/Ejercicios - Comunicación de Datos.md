# Ejercicios - Comunicación de Datos (Enlace)

Problemas resueltos del Tema 3 sobre sincronización, detección de errores y control de flujo.

## Ejercicio 1: Overhead en Transmisión Asíncrona
**Enunciado**: Se desea enviar 500 caracteres ASCII (8 bits/carácter) usando transmisión asíncrona sin paridad (mínimo de bits adicionales). ¿Cuál es el número de bits adicionales y el porcentaje de overhead?

**Solución**:
- Bits por carácter: 1 Start + 8 Datos + 1 Stop = 10 bits.
- Bits adicionales (Overhead): 2 bits por carácter.
- Total bits adicionales: $500 \times 2 = 1000$ bits.
- Total bits enviados: $500 \times 10 = 5000$ bits.
- % Overhead: $(1000 / 5000) \times 100 = 20\%$.

## Ejercicio 2: Cálculo de CRC
**Enunciado**: Dado el mensaje $M = 1101010110$ y el divisor $P = 110101$. Calcula la secuencia CRC (FCS).

**Solución**:
1. El grado del polinomio generador ($P$) es 5 (longitud 6).
2. Añadimos 5 ceros a $M$: $11010101100000$.
3. Realizamos la división binaria (XOR) entre $11010101100000$ y $110101$.
4. El resto obtenido es el FCS. Según los cálculos del PDF, el FCS es $10100$.
5. Secuencia a transmitir: $110101011010100$.

## Ejercicio 3: Probabilidad de Error con Paridad
**Enunciado**: ¿El uso de un bit de paridad mejora la probabilidad de recibir un mensaje correctamente?

**Solución**:
No. La probabilidad de recibir correctamente un mensaje de $L$ bits es $(1-P_b)^L$. Al añadir un bit de paridad, $L$ aumenta (de 8 a 9), por lo que la probabilidad de que la trama llegue sin errores disminuye. Sin embargo, permite **detectar** errores simples, lo que evita procesar datos corruptos.

## Ejercicio 4: Ventana Deslizante y ARQ (P 3.9)
**Enunciado**: Dos nodos usan ventana deslizante de 3 bits ($W=4$). Muestra las ventanas tras:
a) Antes de enviar nada.
b) Tras enviar tramas 0, 1 y 2 y recibir ACKs de 0 y 1.

**Solución**:
- **3 bits de secuencia**: Significa números del 0 al 7.
- **a) Inicio**:
  - Ventana Emisor: `[0, 1, 2, 3]` (puede enviar estas 4).
  - Ventana Receptor: `0` (espera la 0).
- **b) Tras enviar 0, 1, 2 y recibir ACK 0 y 1**:
  - Al recibir ACK 0 y 1, la ventana del emisor se desliza 2 posiciones.
  - Nueva Ventana Emisor: `[2, 3, 4, 5]`. (La 2 ya está enviada pero no confirmada).
  - Ventana Receptor: `2` (ya recibió 0 y 1, espera la 2).

## Ejercicio 5: Velocidad en Nodos Intermedios (P 3.8)
**Enunciado**: Nodo A envía a C pasando por B. Entre A y B: 100 kbps, $W=3$, tramas 1000 bits. Determina la velocidad mínima entre B y C (Parada y Espera) para que B no se sature.

**Solución**:
1. **Tasa de llegada a B (de A)**:
   - Tiempo de transmisión de una trama: $1000 \text{ bits} / 100.000 \text{ bps} = 10 \text{ ms}$.
   - Con $W=3$, A puede enviar 3 tramas seguidas rápido. En promedio, la tasa está limitada por los 100 kbps.
2. **Tasa de salida de B (hacia C)**:
   - B usa Parada y Espera. Para cada trama, tarda: $T_{transmisio_n} + 2 \cdot T_{propagacio_n}$.
   - Para no saturarse: $T_{salida} \leq T_{llegada}$.
   - Resulta que la línea B-C necesita ser más rápida que la A-B porque Parada y Espera pierde mucho tiempo esperando el ACK, mientras que Ventana Deslizante aprovecha mejor el tiempo.

---
**Relacionado**: [Transmisión Asíncrona vs Síncrona](../Notas/Transmisi%C3%B3n%20As%C3%ADncrona%20vs%20S%C3%ADncrona.md), [Protocolos ARQ](../Notas/Protocolos%20ARQ.md)
**Fuente**: [[34_ProblemasTema3.pdf]]
