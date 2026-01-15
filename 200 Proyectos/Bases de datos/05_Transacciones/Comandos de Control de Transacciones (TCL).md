# Comandos de Control de Transacciones (TCL)

Estos son los comandos principales del [Comandos de Control de Transacciones (TCL)](Comandos%20de%20Control%20de%20Transacciones%20%28TCL%29.md) para gestionar una [Transacción](Transacci%C3%B3n.md):

*   **`START TRANSACTION`** o **`BEGIN`**: Inicia una nueva transacción.
*   **`COMMIT`**: Guarda de forma permanente todos los cambios realizados en la transacción actual.
*   **`ROLLBACK`**: Deshace todos los cambios realizados en la transacción actual, restaurando el estado anterior.
*   **`SAVEPOINT nombre_punto`**: Establece un punto de guardado intermedio dentro de la transacción.
*   **`ROLLBACK TO nombre_punto`**: Revierte la transacción hasta el `SAVEPOINT` especificado, sin anular la transacción completa.

---
**Relacionado:** [Transacción](Transacci%C3%B3n.md), [Comandos de Control de Transacciones (TCL)](Comandos%20de%20Control%20de%20Transacciones%20%28TCL%29.md), [Propiedades ACID](Propiedades%20ACID.md)
