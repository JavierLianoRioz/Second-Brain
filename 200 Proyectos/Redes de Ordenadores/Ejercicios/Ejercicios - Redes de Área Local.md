# Ejercicios - Redes de Área Local

Problemas resueltos del Tema 4 sobre topologías, Ethernet, switches y VLANs.

## Ejercicio 1: Rendimiento en Estrella (Conmutación de Circuitos)
**Enunciado**: Transferencia de 1 millón de caracteres (8 bits/carácter) a 64 kbps usando conmutación de circuitos. Calcula el tiempo y velocidad efectiva.

**Solución**:
- Total bits: $10^6 \times 8 = 8,000,000$ bits.
- Tiempo: $8,000,000 / 64,000 = 125$ segundos.
- Velocidad efectiva: 64 kbps (no hay overhead ni paradas en este modelo).

## Ejercicio 2: Tiempo de espera en CSMA/CD
**Enunciado**: Tras una colisión, el adaptador espera $K \times 512$ tiempos de bit. Si $K=100$, ¿cuánto tiempo debe esperar en una red de 10 Mbps y en una de 100 Mbps?

**Solución**:
- **10 Mbps**: Tiempo de bit = $1 / 10^{7}$ s. Espera: $100 \times 512 \times 10^{-7} = 5.12$ ms.
- **100 Mbps**: Tiempo de bit = $1 / 10^{8}$ s. Espera: $100 \times 512 \times 10^{-8} = 512$ $\mu$s.

## Ejercicio 3: Aprendizaje de Direcciones (P 4.6)
**Enunciado**: Switch con tabla vacía. Secuencia: i) B -> E, ii) E -> B, iii) A -> B.

**Solución**:
1. **B envía a E**: El switch no sabe dónde está E. Hace **Flooding** (inunda todos los puertos). Aprende: `MAC_B -> Puerto 2`.
2. **E responde a B**: El switch ya sabe que B está en el Puerto 2. Envía la trama **solo por el Puerto 2**. Aprende: `MAC_E -> Puerto 5`.
3. **A envía a B**: El switch sabe que B está en el Puerto 2. Envía por el Puerto 2. Aprende: `MAC_A -> Puerto 1`.

## Ejercicio 4: Rendimiento Agregado (P 4.3, 4.4, 4.5)
**Enunciado**: 11 nodos (100 Mbps cada uno). Compara el rendimiento total si usamos Switches vs Hubs.

**Solución**:
- **Con Switches (P 4.3)**: Cada puerto es independiente. Rendimiento total = $11 \times 100 = 1100$ Mbps ($1.1$ Gbps).
- **Con Hubs departamentales (P 4.4)**: Cada grupo de equipos comparte 100 Mbps. Si hay 5 grupos, el total es $5 \times 100 = 500$ Mbps.
- **Todo con Hubs (P 4.5)**: Todos comparten el mismo "aire". El rendimiento total de la red entera es de **solo 100 Mbps**, sin importar cuántos equipos haya.

---
**Relacionado**: [[Conceptos de LAN y Control de Acceso]], [[Dispositivos de Interconexión (Hubs vs Switches)]]
**Fuente**: [[44_ProblemasTema4.pdf]]
