# Transacción

Una **transacción** es una secuencia de operaciones ([SQL DML](../03_SQL/SQL_DML.md)) que se ejecutan como una **única unidad lógica de trabajo**.

El principio es "todo o nada": o todas las operaciones se completan con éxito y se confirman (`COMMIT`), o si una falla, todas se deshacen (`ROLLBACK`).

Las transacciones garantizan la integridad y consistencia de la base de datos, y su fiabilidad se describe mediante las [Propiedades ACID](Propiedades%20ACID.md).

---
**Relacionado:** [Propiedades ACID](Propiedades%20ACID.md), [Comandos de Control de Transacciones (TCL)](Comandos%20de%20Control%20de%20Transacciones%20%28TCL%29.md)
