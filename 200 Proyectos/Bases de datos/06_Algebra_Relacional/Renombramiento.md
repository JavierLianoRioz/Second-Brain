---
tags: [theory, relational-algebra, database]
moc: "[00_MOC_Algebra_Relacional](00_MOC_Algebra_Relacional.md)"
status: refined
---
difficulty: intermediate
---

# Renombramiento (ρ)

---

## 🧠 Núcleo del Concepto

El operador de **Renombramiento** (ρ) permite cambiar el nombre de una relación o de sus atributos individuales, facilitando la gestión de expresiones complejas.

*   **Utilidad**: Es indispensable para realizar operaciones sobre la misma relación (auto-joins) o para evitar conflictos de nombres tras un [Producto Cartesiano](Producto_Cartesiano.md).
*   **Identidad**: No altera los datos ni el esquema interno, solo su etiqueta externa.
*   **Equivalencia SQL**: Se traduce como el alias `AS`.

---

## 🔗 Conexiones y Contexto

*   **Se relaciona con:** [Producto Cartesiano](Producto_Cartesiano.md), [Join Algebra](Join_Algebra.md).
*   **Diferencia clave con:** Otras operaciones que transforman datos; esta solo transforma metadatos (nombres).

---

> [!tip] Idea Fuerza (Cierre)
> El renombramiento es el "apodo" técnico: permite que una tabla se llame de otra forma para que no se confunda consigo misma.

---

## 🗺️ Mapa de Contenido
*   Volver a: [00 MOC Algebra Relacional](00_MOC_Algebra_Relacional.md).
