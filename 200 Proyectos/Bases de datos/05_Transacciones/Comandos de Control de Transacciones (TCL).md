# Comandos de Control de Transacciones (TCL)

Estos son los comandos principales del [[Comandos de Control de Transacciones (TCL)]] para gestionar una [[Transacción]]:

*   **`START TRANSACTION`** o **`BEGIN`**: Inicia una nueva transacción.
*   **`COMMIT`**: Guarda de forma permanente todos los cambios realizados en la transacción actual.
*   **`ROLLBACK`**: Deshace todos los cambios realizados en la transacción actual, restaurando el estado anterior.
*   **`SAVEPOINT nombre_punto`**: Establece un punto de guardado intermedio dentro de la transacción.
*   **`ROLLBACK TO nombre_punto`**: Revierte la transacción hasta el `SAVEPOINT` especificado, sin anular la transacción completa.

---
**Relacionado:** [[Transacción]], [[Comandos de Control de Transacciones (TCL)]], [[Propiedades ACID]]
