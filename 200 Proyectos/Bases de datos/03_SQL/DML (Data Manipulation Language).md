# DML (Data Manipulation Language)

El **DML** es el [[Sublenguajes de SQL|sublenguaje de SQL]] usado para gestionar y manipular los datos almacenados en las tablas.

### Comandos Principales

*   `SELECT`: Recupera datos de una o más tablas.
*   `INSERT`: Añade nuevas filas de datos a una tabla.
*   `UPDATE`: Modifica datos en filas existentes.
*   `DELETE`: Elimina filas de una tabla.

A diferencia del [[DDL (Data Definition Language)]], las operaciones DML pueden ser (y a menudo son) parte de una [[Transacción]], lo que permite que puedan ser revertidas con `ROLLBACK`.

### Ejemplos

```sql
-- Insertar
INSERT INTO cliente (id, nombre) VALUES (1, 'Ana');

-- Actualizar
UPDATE cliente SET nombre = 'Ana Gomez' WHERE id = 1;

-- Eliminar
DELETE FROM cliente WHERE id = 1;

-- Consultar
SELECT * FROM cliente WHERE nombre LIKE 'Ana%';
```

---
**Relacionado:** [[Sublenguajes de SQL]], [[Transacción]]
