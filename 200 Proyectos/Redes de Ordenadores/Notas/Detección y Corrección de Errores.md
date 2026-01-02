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

---
**Relacionado**: [[Protocolos ARQ]]
**Fuente**: [[32_Tema3.pdf]]
