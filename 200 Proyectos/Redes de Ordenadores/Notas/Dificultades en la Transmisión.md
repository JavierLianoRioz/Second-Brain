# Dificultades en la Transmisión

La señal recibida no es idéntica a la transmitida debido a diversas degradaciones físicas.

## Principales Dificultades
1. **Atenuación**: Pérdida de fuerza de la señal al viajar por el medio.
   - *Analogía*: Tu voz se oye más floja cuanto más lejos estás de quien te escucha. Necesitas un "megáfono" (amplificador) para llegar lejos.
   - *Población*: Las frecuencias altas "se mueren" antes que las bajas.
2. **Distorsión de Retardo**: Diferentes frecuencias viajan a diferentes velocidades.
   - *Analogía*: Imagina una carrera donde los corredores (frecuencias) salen juntos pero unos llegan mucho antes que otros, desordenando el mensaje final.
3. **Ruido**: Señales extrañas que se mezclan con la nuestra.

## Distancia y Regeneración de Señal
Para alcanzar distancias largas necesitamos dispositivos intermedios:
- **Amplificador (Transmisión Analógica)**: Aumenta la potencia de la señal, pero **también aumenta el ruido**. La relación señal-ruido (SNR) empeora con cada amplificador.
- **Repetidor (Transmisión Digital)**: No solo amplifica, sino que **regenera** la señal (vuelve a crear el 0 o el 1 perfecto). No acumula el ruido de tramos anteriores.

> [!TIP]
> Por esto la transmisión digital es mucho más fiable a largas distancias; podemos "limpiar" la señal en cada salto.

## Tipos de Ruido
- **Térmico (Blanco)**: Inevitable, producido por el calor de los componentes.
  - *Analogía*: El siseo de fondo en una radio antigua.
- **Diafonía (Crosstalk)**: Interferencia de cables vecinos.
  - *Analogía*: Escuchar la conversación de otra persona a través de la pared o por el teléfono.
- **Impulsivo**: Picos de energía cortos y fuertes (rayos, interruptores).
  - *Analogía*: Un portazo ruidoso que te impide oír una palabra suelta en una frase. Es el más peligroso para los errores de bits.

---
**Relacionado**: [Señales Analógicas y Digitales](Se%C3%B1ales%20Anal%C3%B3gicas%20y%20Digitales.md)
**Fuente**: [[22_Tema2.pdf]]
