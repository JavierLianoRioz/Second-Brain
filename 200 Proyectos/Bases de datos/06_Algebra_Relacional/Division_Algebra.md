---
tags: [algebra-relacional, operator, theory]
moc: [[00_MOC_Algebra_Relacional]]
status: refined
difficulty: advanced
---

# División (÷)

---

## 🧠 Núcleo del Concepto

La **División** (÷) es una operación binaria compleja que se utiliza para consultas de tipo "para todo" o "todos los que".

*   **Propósito**: Identificar las tuplas de una relación $R$ que están asociadas con **todas** las tuplas de una relación $S$.
*   **Condición**: El esquema de $S$ debe ser un subconjunto del esquema de $R$.
*   **Complejidad**: Es la operación más difícil de expresar en álgebra básica y en SQL (suele requerir subconsultas anidadas o `NOT EXISTS`).

---

## 🔗 Conexiones y Contexto

*   **Se relaciona con:** [Join Algebra](Join_Algebra.md), [Diferencia Operador](Diferencia_Operador.md).
*   **Ejemplo Clásico**: "¿Qué proveedores suministran **todas** las piezas?".

---

> [!tip] Idea Fuerza (Cierre)
> La división es el filtro del "pleno": solo pasan los que han completado la colección entera.

---

## 🗺️ Mapa de Contenido
*   Volver a: [00 MOC Algebra Relacional](00_MOC_Algebra_Relacional.md).
