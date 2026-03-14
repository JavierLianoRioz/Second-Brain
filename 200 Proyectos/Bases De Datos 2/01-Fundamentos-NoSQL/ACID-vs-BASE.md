# ACID vs BASE

La elección de una base de datos depende del modelo de consistencia y garantías transaccionales requeridas.

### ACID (Modelo Relacional)
Prioriza la integridad y la consistencia fuerte.
*   **A**tomicidad: Todo o nada.
*   **C**onsistencia: Estado válido tras cada transacción.
*   **I**solation (Aislamiento): Las transacciones no interfieren entre sí.
*   **D**urabilidad: Los cambios persisten tras fallos.

### BASE (Modelo NoSQL)
Prioriza la disponibilidad y la escalabilidad sobre la consistencia inmediata.
*   **B**asically **A**vailable: El sistema garantiza una respuesta.
*   **S**oft state: El estado puede cambiar sin intervención externa debido a la propagación de datos.
*   **E**ventual consistency: El sistema será consistente en algún momento futuro si no hay nuevas actualizaciones.

---
### Ejemplo de Comparación
En un sistema bancario se prefiere **ACID** para evitar saldos negativos. En una red social (likes) se acepta **BASE** para permitir una respuesta inmediata a millones de usuarios. Ambos modelos se eligen según las necesidades descritas en la [Introducción a NoSQL](NoSQL-Introduction.md) y las limitaciones del [Teorema CAP](CAP-Theorem.md).
