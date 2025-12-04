# UPDATE

Comando [[SQL_DML]] para modificar datos existentes.

> [!IMPORTANT]
> Siempre usa [[SQL_WHERE]]. Si lo olvidas, actualizarás **todas** las filas.

## Sintaxis
```sql
UPDATE tabla SET col1 = val1 WHERE condicion;
```

## Ejemplo
```sql
UPDATE producto SET precio = 20 WHERE id = 5;
```

---
[[SQL_DML]]
