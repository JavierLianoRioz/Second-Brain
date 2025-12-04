# CREATE TABLE

Comando [[SQL_DDL]] para crear una nueva tabla.

## Sintaxis
```sql
CREATE TABLE nombre_tabla (
    columna1 tipo restriccion,
    columna2 tipo restriccion,
    ...
);
```

## Ejemplo
```sql
CREATE TABLE empleado (
    id_empleado INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    salario DECIMAL(10,2)
);
```

---
[[SQL_DDL]]
