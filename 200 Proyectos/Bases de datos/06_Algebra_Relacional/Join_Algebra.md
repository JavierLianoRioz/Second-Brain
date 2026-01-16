---
tags: [algebra-relacional, operator, theory]
moc: [[00_MOC_Algebra_Relacional]]
status: refined
difficulty: advanced
---

# Reunión / Join (⨝)

---

## 🧠 Núcleo del Concepto

El operador de **Reunión** (Join) es una operación binaria que permite combinar tuplas de dos relaciones basándose en una condición de emparejamiento entre sus atributos.

*   **Derivación**: Es equivalente a realizar un [Producto Cartesiano](Producto_Cartesiano.md) seguido de una [Seleccion Operador](Seleccion_Operador.md).
*   **Equivalencia SQL**: Se corresponde directamente con la cláusula [SQL JOIN](../03_SQL/SQL_JOIN.md).
*   **Importancia**: Es la operación fundamental para navegar por el [Modelo Relacional Conceptos](../02_Dise%C3%B1o/Modelo_Relacional_Conceptos.md) a través de claves foráneas.

---

## 🗺️ Tipos de Join

> [!abstract] Variantes Comunes
> 1.  **Theta Join ($R \bowtie\{condición\} S$)**: Usa cualquier predicado de comparación ($<, >, =, \neq$).
> 2.  **Equi Join**: Un subtipo de Theta Join donde solo se usa la igualdad ($=$).
> 3.  **Natural Join ($R \bowtie S$)**: Combina por atributos con el mismo nombre, proyectando una sola vez las columnas duplicadas.

---

## 🔗 Conexiones y Contexto

*   **Se relaciona con:** [SQL JOIN](../03_SQL/SQL_JOIN.md), [Clave Foranea](../02_Dise%C3%B1o/Clave_Foranea.md).
*   **Operación base**: $R \bowtie\{c\} S = \sigma\{c\}(R \times S)$.

---

> [!tip] Idea Fuerza (Cierre)
> El Join es el "pegamento" de las bases de datos relacionales: une piezas separadas para formar una imagen coherente.
