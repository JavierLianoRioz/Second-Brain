# Detección y Corrección de Errores

El control de errores añade redundancia para garantizar la integridad de los datos.

## Tipos de Códigos
- **BEC (Backward Error Correction)**: El receptor detecta el error y pide que se repita.
  - *Analogía*: Decir "¿Qué?" cuando no oyes bien una palabra.
- **FEC (Forward Error Correction)**: El mensaje lleva tanta información extra que el receptor puede arreglar el error él solo.
  - *Analogía*: Un libro con una errata obvia ("El gato beba agua") que tú corriges mentalmente al leer ("bebe") sin preguntar al autor.

## Mecanismos de Detección
- **CRC (Cyclic Redundancy Check)**: El método más robusto.
  - *Analogía*: Como el dígito de control de tu DNI o de una cuenta bancaria. Es una operación matemática que resume todo el mensaje; si un solo bit cambia, el resumen no coincide.

## Transparencia de Datos: Bit Stuffing
¿Qué pasa si el patrón que indica "Aquí termina la trama" (ej. `01111110`) aparece por casualidad dentro de los datos? El receptor se confundiría y cortaría el mensaje antes de tiempo.
- **Solución (Bit Stuffing)**: Cada vez que el emisor ve cinco `1` seguidos en los datos, mete un `0` a la fuerza.
- **Receptor**: Cuando ve cinco `1`, mira el siguiente bit:
  - Si es `0`, lo quita (era relleno).
  - Si es `1`, entonces sí es el patrón de final real.

---
**Relacionado**: [[Protocolos ARQ]]
**Fuente**: [[32_Tema3.pdf]]
