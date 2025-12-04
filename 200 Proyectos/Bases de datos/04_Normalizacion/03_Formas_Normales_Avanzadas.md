# Formas Normales Avanzadas (4FN, 5FN)

Se aplican en escenarios complejos donde persisten redundancias sutiles después de la 3FN.

## 1. Cuarta Forma Normal (4FN)

**Regla**:
1.  Cumplir 3FN.
2.  **Eliminar Dependencias Multivaluadas**: Un atributo no puede determinar dos o más conjuntos de valores independientes.

### Ejemplo: Violación de 4FN
Un `Profesor` enseña varios `Cursos` y habla varios `Idiomas`. Son hechos independientes.

| Profesor | Curso | Idioma |
| :--- | :--- | :--- |
| Ana | Mates | Inglés |
| Ana | Mates | Español |
| Ana | Física | Inglés |
| Ana | Física | Español |

Se genera un producto cartesiano innecesario. Si Ana aprende Francés, hay que añadir filas para todos sus cursos.

### Solución 4FN
Dividir en dos tablas independientes.
1.  `PROFESOR_CURSO` (Profesor, Curso)
2.  `PROFESOR_IDIOMA` (Profesor, Idioma)

---

## 2. Quinta Forma Normal (5FN)

**Regla**:
1.  Cumplir 4FN.
2.  **Eliminar Dependencias de Unión**: La información se puede reconstruir sin pérdida a partir de tablas más pequeñas, pero mantenerla junta genera redundancia.

### Ejemplo: Violación de 5FN
Relación ternaria `Proveedor - Producto - Tienda`.
*   Proveedor A vende Tornillos.
*   Proveedor A vende a Madrid.
*   Madrid vende Tornillos.

Si guardamos `(A, Tornillo, Madrid)` en una sola tabla, podríamos estar forzando una relación que en realidad se deriva de las otras tres.

### Solución 5FN
Descomponer en tres tablas binarias si la relación es reconstruible:
1.  `PROVEEDOR_PRODUCTO` (Quién vende qué)
2.  `PROVEEDOR_TIENDA` (Quién vende dónde)
3.  `PRODUCTO_TIENDA` (Qué se vende dónde)

Si al hacer JOIN de las tres recuperamos la información original exacta, entonces la descomposición es válida y necesaria.
