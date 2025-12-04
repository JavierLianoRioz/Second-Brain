# Transacción

Una **transacción** es una secuencia de operaciones ([[SQL_DML]]) que se ejecutan como una **única unidad lógica de trabajo**.

El principio es "todo o nada": o todas las operaciones se completan con éxito y se confirman (`COMMIT`), o si una falla, todas se deshacen (`ROLLBACK`).

Las transacciones garantizan la integridad y consistencia de la base de datos, y su fiabilidad se describe mediante las [[Propiedades ACID]].

---
**Relacionado:** [[Propiedades ACID]], [[Comandos de Control de Transacciones (TCL)]]
