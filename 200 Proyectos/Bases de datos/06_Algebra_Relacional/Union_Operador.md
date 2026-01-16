---
tags: [theory, relational-algebra, database]
moc: "[00_MOC_Algebra_Relacional](00_MOC_Algebra_Relacional.md)"
status: refined
---
difficulty: basic
---

# Unión (∪)

---

## 🧠 Núcleo del Concepto

La **Unión** (∪) es una operación binaria que combina las tuplas de dos relaciones compatibles en una única relación resultante.

*   **Compatibilidad de Esquema**: Ambas relaciones deben tener el mismo número de atributos y dominios compatibles (tipos de datos idénticos en el mismo orden).
*   **Eliminación de Duplicados**: Al ser una operación de conjuntos, los duplicados se eliminan automáticamente.
*   **Equivalencia SQL**: Se corresponde con el comando `UNION`.

---

## 🔗 Conexiones y Contexto

*   **Se relaciona con:** [Interseccion Operador](Interseccion_Operador.md), [Diferencia Operador](Diferencia_Operador.md).
*   **Requisito técnico:** Solo se puede aplicar si las relaciones son "unión-compatibles".

---

> [!tip] Idea Fuerza (Cierre)
> La unión suma mundos: junta dos tablas para crear una lista maestra sin repeticiones.

---

## 🗺️ Mapa de Contenido
*   Volver a: [00 MOC Algebra Relacional](00_MOC_Algebra_Relacional.md).
