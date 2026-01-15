# Propiedades ACID

**ACID** es un acrónimo que describe las cuatro propiedades que garantizan la fiabilidad de una [Transacción](Transacci%C3%B3n.md):

1.  **Atomicidad (Atomicity):** La transacción es indivisible. O se ejecuta en su totalidad o no se ejecuta en absoluto.
2.  **Consistencia (Consistency):** La transacción lleva a la base de datos de un estado válido a otro, cumpliendo todas las [restricciones](../03_SQL/Constraints_SQL.md).
3.  **Aislamiento (Isolation):** Las transacciones concurrentes no interfieren entre sí. Cada una se ejecuta como si estuviera sola.
4.  **Durabilidad (Durability):** Una vez que una transacción se confirma (`COMMIT`), los cambios son permanentes y sobreviven a fallos del sistema.

---
**Relacionado:** [Transacción](Transacci%C3%B3n.md), [Comandos de Control de Transacciones (TCL)](Comandos%20de%20Control%20de%20Transacciones%20%28TCL%29.md)
