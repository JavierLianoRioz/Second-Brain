# Selección (Álgebra Relacional)

La **Selección** (denotada por **σ**, sigma) es una operación unaria que selecciona las tuplas (filas) de una relación que satisfacen una condición específica.

### Sintaxis
`σ condición (R)`

### Ejemplo
Dada la relación **EMPLEADO**:

| ID | NOMBRE | DEPTO  |
|----|--------|--------|
| 1  | Ana    | Ventas |
| 2  | Luis   | IT     |

`σ DEPTO="IT" (EMPLEADO)`

**Resultado:**

| ID | NOMBRE | DEPTO |
|----|--------|-------|
| 2  | Luis   | IT    |

Equivale a la cláusula `WHERE` en SQL.

---
**Relacionado:** [[Álgebra Relacional]], [[Proyección (Álgebra Relacional)]]
