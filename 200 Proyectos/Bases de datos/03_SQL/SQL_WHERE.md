# SQL WHERE

Cláusula para filtrar filas en [SELECT Basico](SELECT_Basico.md), [UPDATE](UPDATE.md) y [DELETE](DELETE.md).

## Operadores
*   `=`, `<>`, `>`, `<`
*   `IN`: Lista de valores.
*   `BETWEEN`: Rango.
*   `LIKE`: Patrones de texto (`%`).
*   `IS NULL`: Valores nulos.

## Ejemplo
```sql
SELECT * FROM producto WHERE precio > 50 AND categoria = 'Hogar';
```

---
[SELECT Basico](SELECT_Basico.md)
