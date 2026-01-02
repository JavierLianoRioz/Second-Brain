# Protocolos ARQ

Los protocolos **ARQ (Automatic Repeat Request)** combinan detección de errores y control de flujo para lograr un enlace fiable mediante retransmisiones.

## Variantes Principales
1. **ARQ con Vuelta Atrás N (Go-Back N)**:
   - *Analogía*: Dictado en clase. Si el alumno se pierde en la palabra 5, el profesor para y vuelve a dictar **todo** desde la palabra 5.
   - *Ventaja*: El receptor es muy tonto/simple, no necesita guardar nada extra.
2. **ARQ con Rechazo Selectivo (Selective Reject)**:
   - *Analogía*: Dictado eficiente. Si el alumno no entiende la palabra 5, el profesor termina la frase y al final solo repite la palabra 5.
   - *Ventaja*: Ahorra tiempo, pero el alumno (receptor) tiene que ser más listo (tener buffer de reordenación).

---
**Relacionado**: [[Control de Flujo]], [[Detección y Corrección de Errores]]
**Fuente**: [[32_Tema3.pdf]]
