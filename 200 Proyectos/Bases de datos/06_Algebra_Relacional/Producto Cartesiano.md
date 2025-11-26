# Producto Cartesiano

El **Producto Cartesiano** (denotado por **×**) es una operación binaria que combina cada tupla de una relación con todas las tuplas de otra relación.

Si la relación R tiene N tuplas y la relación S tiene M tuplas, el resultado tendrá **N × M** tuplas.

### Sintaxis
`R × S`

### Ejemplo
**R**: {A, B}, **S**: {1, 2}
`R × S` = {(A,1), (A,2), (B,1), (B,2)}

Es la base conceptual para el [[Join (Combinación)]]. Equivale a `CROSS JOIN` en SQL o listar tablas en `FROM` sin condición.

---
**Relacionado:** [[Álgebra Relacional]], [[Join (Combinación)]]
