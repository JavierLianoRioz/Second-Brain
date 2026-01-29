---
tags: [concept, neuro-efficiency, db-design]
moc: "[00_MOC_Diseño](00_MOC_Diseño.md)"
status: refined
difficulty: intermediate
---

# Entidad

---

## 🧠 Núcleo del Concepto
Una **Entidad** representa cualquier objeto, persona o evento del mundo real (ya sea físico o conceptual) con existencia independiente y del cual interesa almacenar información específica.

*   **Existencia Autónoma:** No depende de otra cosa para ser identificada (ej. un `Cliente` existe por sí mismo).
*   **Tipología:** Pueden ser tangibles (físicas como `Vehículo`) o intangibles (abstractas como `Venta`).
*   **Representación:** En la implementación física, cada instancia de una entidad se convertirá en una fila de una **Tabla**.

---

## 🗺️ Anclaje Visual (Dual Coding)
> [!abstract] Representación en Diagrama ER
> ```mermaid
> erDiagram
>     ENTIDAD {
>         string atributo_1
>         string atributo_2
>     }
> ```

---

## 🔗 Conexiones y Contexto
*   **Se relaciona con:** [Atributo](Atributo.md) (las propiedades que describen a la entidad) y [Relación ER](Relacion_ER.md) (cómo interactúan las entidades).
*   **Diferencia clave con:** El **Atributo**, que es una propiedad atómica y no tiene existencia independiente fuera de la entidad.

---

> [!tip] Idea Fuerza (Cierre)
> Las entidades son los "sustantivos" del ecosistema de datos; definen el QUÉ antes de preocuparnos por el CÓMO.
