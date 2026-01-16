---
tags: [algebra-relacional, operator, theory]
moc: [[00_MOC_Algebra_Relacional]]
status: refined
difficulty: intermediate
---

# Producto Cartesiano (×)

---

## 🧠 Núcleo del Concepto

El **Producto Cartesiano** (×) es una operación binaria que combina cada tupla de la primera relación con todas las tuplas de la segunda.

*   **Crecimiento Exponencial**: Si $R$ tiene $n$ filas y $S$ tiene $m$ filas, el resultado tendrá $n \times m$ filas.
*   **Esquema Resultante**: La relación resultante contiene todos los atributos de $R$ seguidos de todos los de $S$.
*   **Se relaciona con:** [Join Algebra](Join_Algebra.md), [Clave Foranea](../02_Dise%C3%B1o/Clave_Foranea.md).
*   **Advertencia**: Es una operación muy costosa si no se filtra inmediatamente con una [Seleccion Operador](Seleccion_Operador.md).

---

> [!tip] Idea Fuerza (Cierre)
> El producto cartesiano es la "cita a ciegas total": todos con todos, sin filtros.

---

## 🗺️ Mapa de Contenido
*   Volver a: [00 MOC Algebra Relacional](00_MOC_Algebra_Relacional.md).
