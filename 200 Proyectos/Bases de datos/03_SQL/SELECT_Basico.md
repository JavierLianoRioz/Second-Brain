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
*   [[SQL_WHERE]]: Filtrar filas.
*   `ORDER BY`: Ordenar.
*   `LIMIT`: Paginación.


## Base Teórica
Este comando implementa las operaciones del [[Algebra_Relacional_Concepto]]:
*   `WHERE` implementa la [[Seleccion_Operador]].
*   La lista de columnas implementa la [[Proyeccion_Operador]].

---
[[00_MOC_SQL]]
