# SELECT Básico

Comando para recuperar datos.

## Estructura
```sql
SELECT columnas FROM tabla;
```

## Ejemplo
```sql
SELECT nombre, precio FROM producto;
```

## Clausulas
*   [SQL_WHERE](SQL_WHERE.md): Filtrar filas.
*   `ORDER BY`: Ordenar.
*   `LIMIT`: Paginación.


## Base Teórica
Este comando implementa las operaciones del [Algebra_Relacional_Concepto](../06_Algebra_Relacional/Algebra_Relacional_Concepto.md):
*   `WHERE` implementa la [Seleccion_Operador](../06_Algebra_Relacional/Seleccion_Operador.md).
*   La lista de columnas implementa la [Proyeccion_Operador](../06_Algebra_Relacional/Proyeccion_Operador.md).

---
[00_MOC_SQL](00_MOC_SQL.md)
