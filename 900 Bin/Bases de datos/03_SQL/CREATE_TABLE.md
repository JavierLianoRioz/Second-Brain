# CREATE TABLE

> [!WARNING]
> **NO ENTRA EN EL EXAMEN FINAL (DDL)**


Comando [SQL DDL](SQL_DDL.md) para crear una nueva tabla.

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
[SQL DDL](SQL_DDL.md)
