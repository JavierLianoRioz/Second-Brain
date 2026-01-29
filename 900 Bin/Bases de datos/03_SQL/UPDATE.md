# UPDATE

Comando [SQL DML](SQL_DML.md) para modificar datos existentes.

> [!IMPORTANT]
> Siempre usa [SQL WHERE](SQL_WHERE.md). Si lo olvidas, actualizarás **todas** las filas.

## Sintaxis
```sql
UPDATE tabla SET col1 = val1 WHERE condicion;
```

## Ejemplo
```sql
UPDATE producto SET precio = 20 WHERE id = 5;
```

---
[SQL DML](SQL_DML.md)
