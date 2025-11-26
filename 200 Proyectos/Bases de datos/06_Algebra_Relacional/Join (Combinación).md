# Join (Combinación)

El **Join** (denotado por **⨝**) es una operación utilizada para combinar tuplas de dos relaciones basándose en un atributo común o una condición.

Es esencialmente un [[Producto Cartesiano]] seguido de una [[Selección (Álgebra Relacional)]].

### Tipos
*   **Theta Join:** Condición general (e.g., A > B).
*   **Equi Join:** Condición de igualdad (=).
*   **Natural Join:** Igualdad en todos los atributos con el mismo nombre, eliminando columnas duplicadas.

### Ejemplo (Natural Join)
**EMPLEADO** (ID, Nombre, ID_Depto) ⨝ **DEPTO** (ID_Depto, Nombre_Depto)

Combina empleados con sus departamentos donde `EMPLEADO.ID_Depto = DEPTO.ID_Depto`.

Equivale a `INNER JOIN` en SQL.

---
**Relacionado:** [[Álgebra Relacional]], [[Producto Cartesiano]]
