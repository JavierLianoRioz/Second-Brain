---
tags: [theory, relational-algebra, database]
moc: [[00_MOC_Algebra_Relacional]]
status: refined
difficulty: advanced
---

# Álgebra Relacional

---

## 🧠 Núcleo del Concepto

El **Álgebra Relacional** es un lenguaje de consulta **procedural** que define un conjunto de operaciones sobre relaciones, donde cada operación toma una o más relaciones como entrada y produce una nueva relación como salida.

*   **Fundamento de SQL**: Es el andamiaje teórico que sustenta el funcionamiento del motor de consultas (especialmente de [SQL DML](../03_SQL/SQL_DML.md)).
*   **Procedural vs. Declarativo**: A diferencia de SQL (declarativo), el álgebra especifica *los pasos* (el cómo) para obtener el resultado.
*   **Clausura**: Todas las operaciones resultan en una relación, lo que permite el anidamiento de expresiones.

---

## 🗺️ Anclaje Visual (Dual Coding)

> [!abstract] Jerarquía de Operaciones
> 
> ```mermaid
> graph TD
>     AR[Álgebra Relacional] --> Fund[Fundamentales]
>     AR --> Deriv[Derivadas]
>     
>     Fund --> S["Selección (σ)"]
>     Fund --> P["Proyección (π)"]
>     Fund --> UC["Unión / Producto (∪, ×)"]
>     
>     Deriv --> J["Join (⨝)"]
>     Deriv --> I["Intersección (∩)"]
>     Deriv --> D["División (÷)"]
>     
>     style AR fill:#f9f,stroke:#333
> ```

---

## 🔗 Conexiones y Contexto

*   **Se relaciona con:** [Modelo Relacional Conceptos](../02_Dise%C3%B1o/Modelo_Relacional_Conceptos.md), [SQL SELECT](../03_SQL/SELECT_Basico.md).
*   **Equivalencias SQL:**
    *   **Selección (σ)** ↔ [SQL WHERE](../03_SQL/SQL_WHERE.md)
    *   **Proyección (π)** ↔ [SQL SELECT](../03_SQL/SELECT_Basico.md) (selección de columnas)
    *   **Reunión (⨝)** ↔ [SQL JOIN](../03_SQL/SQL_JOIN.md)

---

> [!tip] Idea Fuerza (Cierre)
> Si SQL es el lenguaje que hablamos con la base de datos, el Álgebra Relacional es la matemática que la base de datos usa para "pensar".

---

## 🗺️ Mapa de Contenido
*   Para más detalle sobre operadores específicos, ver: [00 MOC Algebra Relacional](00_MOC_Algebra_Relacional.md).
