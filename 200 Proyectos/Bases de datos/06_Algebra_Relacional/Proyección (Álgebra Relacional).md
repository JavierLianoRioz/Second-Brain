# Proyección (Álgebra Relacional)

La **Proyección** (denotada por **π**, pi) es una operación unaria que selecciona ciertas columnas (atributos) de una relación y descarta las demás. Elimina tuplas duplicadas del resultado.

### Sintaxis
`π columna1, columna2 (R)`

### Ejemplo
Dada la relación **EMPLEADO**:

| ID | NOMBRE | DEPTO  |
|----|--------|--------|
| 1  | Ana    | Ventas |
| 2  | Luis   | IT     |

`π NOMBRE (EMPLEADO)`

**Resultado:**

| NOMBRE |
|--------|
| Ana    |
| Luis   |

Equivale a la cláusula `SELECT DISTINCT` en SQL.

---
**Relacionado:** [[Álgebra Relacional]], [[Selección (Álgebra Relacional)]]
