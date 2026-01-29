---
tags: [theory, relational-algebra, database]
moc: "[00_MOC_Algebra_Relacional](00_MOC_Algebra_Relacional.md)"
status: refined
---
difficulty: basic
---

# Diferencia (–)

---

## 🧠 Núcleo del Concepto

La **Diferencia** (–) es una operación binaria que devuelve las tuplas que están presentes en la primera relación pero no en la segunda.

*   **Compatibilidad**: Al igual que la unión, requiere que ambas relaciones sean unión-compatibles (mismo esquema).
*   **Orden Crítico**: $R - S$ no es lo mismo que $S - R$ (no es conmutativa).
*   **Equivalencia SQL**: Se traduce como `EXCEPT` o `MINUS` (dependiendo del SGBD).

---

## 🔗 Conexiones y Contexto

*   **Se relaciona con:** [Union Operador](Union_Operador.md), [Interseccion Operador](Interseccion_Operador.md).
*   **Aplicación**: Útil para encontrar "lo que falta" o elementos que no cumplen cierta condición.

---

> [!tip] Idea Fuerza (Cierre)
> La diferencia es la resta lógica: de este grupo, quítame todos los que aparezcan en este otro.

---

## 🗺️ Mapa de Contenido
*   Volver a: [00 MOC Algebra Relacional](00_MOC_Algebra_Relacional.md).
