---
tags: [concept, neuro-efficiency, db-design]
moc: "[00_MOC_Diseño](00_MOC_Diseño.md)"
status: refined
difficulty: intermediate
---

# Modelo Relacional: Conceptos

---

## 🧠 Núcleo del Concepto
El **Modelo Relacional** organiza la información en colecciones de tablas (relaciones) bidimensionales, basándose en la teoría matemática de conjuntos.

*   **Estructura:** Los datos se guardan en **Tuplas** (filas) y **Atributos** (columnas) dentro de **Tablas**.
*   **Identificación:** Cada fila es única gracias a la [Clave Primaria](Clave_Primaria.md).
*   **Relación:** Las tablas se vinculan mediante [Clave Foránea](Clave_Foranea.md), permitiendo la navegación de datos sin duplicidad innecesaria.

---

## 🗺️ Anclaje Visual (Dual Coding)
> [!abstract] Correspondencia Conceptual
> ```mermaid
> graph LR
>     A[Entidad ER] --> B[Tabla Relacional]
>     C[Atributo ER] --> D[Columna Relacional]
>     E[Identificador ER] --> F[Clave Primaria PK]
> ```

---

## 🔗 Conexiones y Contexto
*   **Se relaciona con:** [Transformación ER a Relacional](Transformacion_ER_a_Relacional.md) (su origen) y [Normalización Objetivos](../04_Normalizacion/Normalizacion_Objetivos.md) (su refinamiento).
*   **Diferencia clave con:** **SGBD**, que es el software que gestiona el modelo; el Modelo Relacional es la estructura lógica en sí.

---

> [!tip] Idea Fuerza (Cierre)
> En el modelo relacional, la potencia reside en la sencillez: todo es una tabla y toda tabla tiene su clave.
