# SQL: Consultas (SELECT)

`SELECT` es el comando más potente y utilizado. Permite recuperar y transformar datos.

## Estructura Básica

El orden de escritura es fijo:

```sql
SELECT columnas        -- 4. Qué mostrar
FROM tabla             -- 1. De dónde sacar datos
WHERE condiciones      -- 2. Qué filas filtrar
GROUP BY columnas      -- 3. Cómo agrupar
HAVING condiciones     -- 5. Qué grupos filtrar
ORDER BY columnas      -- 6. Cómo ordenar
LIMIT n;               -- 7. Cuántos mostrar
```

---

## 1. Filtrado y Ordenación

### WHERE (Filtro de filas)
Operadores: `=`, `<>`, `>`, `<`, `IN`, `BETWEEN`, `LIKE`, `IS NULL`.

```sql
SELECT * FROM producto
WHERE precio > 50 AND categoria = 'Hogar';

-- Búsqueda de texto (empieza por 'Silla')
SELECT * FROM producto WHERE nombre LIKE 'Silla%';
```

### ORDER BY (Ordenación)
`ASC` (ascendente, por defecto) o `DESC` (descendente).

```sql
SELECT nombre, precio FROM producto
ORDER BY precio DESC, nombre ASC;
```

### LIMIT (Paginación)
Limita el número de resultados.

```sql
SELECT * FROM cliente LIMIT 5 OFFSET 10; -- Página 3 (filas 11-15)
```

---

## 2. Agrupación (GROUP BY)

Agrupa filas con valores idénticos para realizar cálculos sobre ellas (COUNT, SUM, AVG, MAX, MIN).

```sql
-- Total de ventas por cliente
SELECT id_cliente, SUM(total) as total_gastado
FROM pedido
GROUP BY id_cliente;
```

### HAVING (Filtro de grupos)
Filtra **después** de agrupar. `WHERE` no sirve para agregaciones.

```sql
-- Clientes que han gastado más de 500€
SELECT id_cliente, SUM(total) as total_gastado
FROM pedido
GROUP BY id_cliente
HAVING SUM(total) > 500;
```

---

## 3. Combinación de Tablas (JOINS)

Vincula datos de múltiples tablas.

*   **INNER JOIN**: Solo filas que coinciden en ambas tablas.
*   **LEFT JOIN**: Todas las filas de la tabla izquierda, y las coincidentes de la derecha (o NULL).
*   **RIGHT JOIN**: Todas las de la derecha.

```sql
SELECT c.nombre, p.fecha, p.total
FROM cliente c
INNER JOIN pedido p ON c.id_cliente = p.id_cliente
WHERE p.total > 100;
```
