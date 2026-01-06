# Transmisión Asíncrona vs Síncrona

La sincronización es fundamental para que el receptor sepa exactamente cuándo muestrear cada bit.

## Transmisión Asíncrona
- **Unidad**: Carácter a carácter (pequeños trozos).
  - *Analogía*: Código Morse manual o escribir a máquina. Das un golpe (Start), envías la letra, y esperas (Stop). Cada letra se sincroniza sola.
- **Eficiencia**: Baja (mucho overhead). Es como enviar cartas donde el sobre pesa más que el mensaje.

## Transmisión Síncrona
- **Unidad**: Bloques grandes (Tramas).
  - *Analogía*: Una orquesta con un director o un metrónomo. Emisor y receptor van al mismo ritmo exacto.
- **Transparencia (Bit Stuffing)**: Evita que los datos se confundan con el final de la trama.
  - *Ejemplo*: Si la señal de "PARAN" es cinco '1's seguidos, el emisor mete un '0' falso cada vez que ve cinco '1's para que no se malinterprete como el final. El receptor quita ese '0' sobrante.

---
**Relacionado**: [[Detección y Corrección de Errores]], [[Control de Flujo]]
**Fuente**: [[32_Tema3.pdf]]
