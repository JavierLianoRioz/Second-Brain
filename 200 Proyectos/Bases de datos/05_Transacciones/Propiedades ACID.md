# Propiedades ACID

**ACID** es un acrónimo que describe las cuatro propiedades que garantizan la fiabilidad de una [[Transacción]]:

1.  **Atomicidad (Atomicity):** La transacción es indivisible. O se ejecuta en su totalidad o no se ejecuta en absoluto.
2.  **Consistencia (Consistency):** La transacción lleva a la base de datos de un estado válido a otro, cumpliendo todas las [[Constraints_SQL|restricciones]].
3.  **Aislamiento (Isolation):** Las transacciones concurrentes no interfieren entre sí. Cada una se ejecuta como si estuviera sola.
4.  **Durabilidad (Durability):** Una vez que una transacción se confirma (`COMMIT`), los cambios son permanentes y sobreviven a fallos del sistema.

---
**Relacionado:** [[Transacción]], [[Comandos de Control de Transacciones (TCL)]]
