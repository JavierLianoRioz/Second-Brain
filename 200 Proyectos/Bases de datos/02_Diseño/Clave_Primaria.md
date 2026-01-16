---
tags: [concept, neuro-efficiency, db-design]
moc: "[00_MOC_Diseño](00_MOC_Diseño.md)"
status: refined
difficulty: easy
---

# Clave Primaria (PK)

---

## 🧠 Núcleo del Concepto
La **Clave Primaria (PK)** es el atributo (o conjunto de ellos) que identifica de forma **única e inequívoca** a cada registro dentro de una tabla.

*   **Unicidad y No Nulo:** No pueden existir duplicados y ningún componente de la PK puede ser `NULL`.
*   **Minimalidad:** Debe estar compuesta por el menor número de atributos posibles para garantizar la identificación.
*   **Estabilidad:** Se recomienda el uso de claves subrogadas (IDs numéricos autoincrementales) frente a claves naturales (ej. DNI) para evitar cambios estructurales.

---

## 🗺️ Anclaje Visual (Dual Coding)
> [!abstract] Identificación Única
> ```mermaid
> graph LR
>     PK[ID_1] --> F1(Fila 1)
>     PK2[ID_2] --> F2(Fila 2)
>     style PK fill:#f9f,stroke:#333
>     style PK2 fill:#f9f,stroke:#333
> ```

---

## 🔗 Conexiones y Contexto
*   **Se relaciona con:** [Clave Foránea](Clave_Foranea.md) (que apunta a una PK) y [Entidad](Entidad.md) (el identificador ER se convierte en PK).
*   **Diferencia clave con:** **Clave Única**, que permite nulos y no es el identificador principal de la fila.

---

> [!tip] Idea Fuerza (Cierre)
> La PK es el "ancla" de la integridad: sin ella, los datos son una masa amorfa sin identidad.
