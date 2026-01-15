# Ejercicios - Medios de Transmisión

Problemas resueltos del Tema 2 sobre la capa física y medios de transmisión.

## Ejercicio 1: Relación Frecuencia y Periodo
**Enunciado**: Una señal periódica tiene una frecuencia de 1 KHz. ¿Cuál es su periodo?

**Solución**:
El periodo ($T$) es la inversa de la frecuencia ($f$):
$T = 1 / f$
$T = 1 / 1000 \text{ Hz} = 10^{-3} \text{ s} = 1 \text{ ms}$

## Ejercicio 2: Modos de Transmisión (Teclado)
**Enunciado**: Razone el modo de transmisión que implica la comunicación entre un PC y un teclado.

**Solución**:
- Caso **Simplex**: Teclados antiguos (IBM XT 1981) donde la comunicación era solo del teclado al PC.
- Caso **Half-duplex**: Teclados modernos (IBM MF-II 1987) que reciben información del PC para activar LEDs (Bloq Mayús, etc.), por lo que el intercambio es bidireccional pero no necesariamente simultáneo.

## Ejercicio 3: Polaridad en Fibra Óptica
**Enunciado**: Razone el motivo por el que, habitualmente, los cables de fibra empleados en enlaces punto a punto tienen dos fibras y su polaridad es importante.

**Solución**:
Piénsalo como una carretera de sentido único. Si quieres ir y volver (comunicación bidireccional), necesitas dos carriles (dos hilos de fibra).
- Una fibra es para **TX (Tx-emisión)**.
- Otra fibra es para **RX (Rx-recepción)**.
**La Polaridad**: Es vital conectar el "emisor" de un lado con el "receptor" del otro. Si conectas TX con TX, es como si dos personas intentaran hablar por el mismo tubo a la vez sin que nadie escuche en el otro extremo: no hay comunicación.

---
**Relacionado**: [Señales Analógicas y Digitales](../Notas/Se%C3%B1ales%20Anal%C3%B3gicas%20y%20Digitales.md), [Tipos de Medios de Transmisión](../Notas/Tipos%20de%20Medios%20de%20Transmisi%C3%B3n.md)
**Fuente**: [[26_ProblemasTema2.pdf]]
