# SQL WHERE

Cláusula para filtrar filas en [[SELECT_Basico]], [[UPDATE]] y [[DELETE]].

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
[[SELECT_Basico]]
