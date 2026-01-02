# Ejercicios - Capa de Transporte

Problemas resueltos del Tema 6 sobre TCP, UDP y ventanas de transmisión.

## Ejercicio 1: Fragmentación vs Reordenación
**Enunciado**: ¿Si IP se encarga de la fragmentación, TCP ya no tiene que preocuparse por el orden?

**Solución**: No. Son conceptos distintos. El receptor IP reensambla los fragmentos de un **mismo datagrama** para entregarlo entero. Sin embargo, diferentes datagramas (cada uno con su segmento TCP) pueden viajar por rutas distintas y llegar desordenados. **TCP** debe usar sus números de secuencia para reordenar los segmentos del flujo antes de entregarlos a la aplicación.

## Ejercicio 2: Tamaño Máximo de Segmento (MSS)
**Enunciado**: ¿Por qué la carga útil máxima de TCP son 65.495 bytes?

**Solución**: El campo de longitud total de la cabecera IP tiene 16 bits (máximo 65.535 bytes).
- Restamos 20 bytes de la cabecera IP $\to$ 65.515 bytes.
- Restamos 20 bytes (mínimo) de la cabecera TCP $\to$ 65.495 bytes.

## Ejercicio 3: Throughput y Ventana TCP
**Enunciado**: Con un RTT de 100 ms y una ventana de 32 KB, ¿cuál es el throughput máximo?

**Solución**:
- Datos por RTT: 32 KB = $32 \times 1024 = 32.768$ bytes.
- Tiempo: 0,1 s.
- Throughput: $(32.768 \times 8) / 0,1 = 2.621.440$ bps $\approx$ 2,62 Mbps.

## Ejercicio 4: Ventana y Delay (P 6.2 logic)
**Enunciado**: ¿Cómo afecta el tamaño de la ventana al rendimiento si el retardo es muy alto (ej. Satélite)?

**Solución**:
- En satélites, el RTT es de unos 500 ms.
- Si la ventana ($W$) es pequeña (ej. 64 KB), el emisor enviará los 64 KB muy rápido y luego tendrá que esperar 500 ms sin hacer nada hasta que llegue el primer ACK.
- **Conclusión**: En redes de "tubo largo" (alto retardo), necesitas ventanas gigantes ($W$ muy grande) para mantener el tubo lleno y que la velocidad no caiga drásticamente.

---
**Relacionado**: [[Control de Flujo, Errores y Congestión en TCP]]
**Fuente**: [[64_ProblemasTema6.pdf]]
