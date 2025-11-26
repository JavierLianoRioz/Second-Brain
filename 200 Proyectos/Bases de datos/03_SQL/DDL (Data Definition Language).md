# DDL (Data Definition Language)

El **DDL** es el [[Sublenguajes de SQL|sublenguaje de SQL]] que se utiliza para definir y gestionar la estructura de los objetos de la base de datos.

### Comandos Principales

*   `CREATE`: Crea nuevos objetos (e.g., `CREATE TABLE ...`).
*   `ALTER`: Modifica la estructura de un objeto existente (e.g., `ALTER TABLE ... ADD COLUMN ...`).
*   `DROP`: Elimina permanentemente un objeto (e.g., `DROP TABLE ...`).
*   `TRUNCATE`: Elimina todas las filas de una tabla de forma rápida (no es reversible como `DELETE`).

### Ejemplos

```sql
-- Crear una tabla
CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Modificar una tabla
ALTER TABLE cliente ADD COLUMN email VARCHAR(100);

-- Eliminar una tabla
DROP TABLE cliente;
```

---
**Relacionado:** [[Sublenguajes de SQL]], [[Restricciones (Constraints) en SQL]]
