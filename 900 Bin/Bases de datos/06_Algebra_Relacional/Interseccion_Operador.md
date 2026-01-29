---
tags: [theory, relational-algebra, database]
moc: "[00_MOC_Algebra_Relacional](00_MOC_Algebra_Relacional.md)"
status: refined
---
difficulty: intermediate
---

# Intersección (∩)

---

## 🧠 Núcleo del Concepto

La **Intersección** (∩) es una operación binaria que devuelve las tuplas que están presentes simultáneamente en dos relaciones.

*   **Derivación**: Se considera una operación derivada, ya que $R \cap S$ puede expresarse como $R - (R - S)$.
*   **Compatibilidad**: Al igual que la unión y la diferencia, requiere que las relaciones sean unión-compatibles.
*   **Equivalencia SQL**: Se traduce como el comando `INTERSECT`.

---

## 🔗 Conexiones y Contexto

*   **Se relaciona con:** [Union Operador](Union_Operador.md), [Diferencia Operador](Diferencia_Operador.md).
*   **Diferencia clave con:** [Union Operador](Union_Operador.md), que suma; la intersección solo se queda con lo común.

---

> [!tip] Idea Fuerza (Cierre)
> La intersección busca los "puntos en común": solo lo que aparece en ambas listas sobrevive.

---

## 🗺️ Mapa de Contenido
*   Volver a: [00 MOC Algebra Relacional](00_MOC_Algebra_Relacional.md).
