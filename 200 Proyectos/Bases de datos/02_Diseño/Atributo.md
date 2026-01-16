---
tags: [concept, neuro-efficiency, db-design]
moc: "[00_MOC_Diseño](00_MOC_Diseño.md)"
status: refined
difficulty: easy
---

# Atributo

---

## 🧠 Núcleo del Concepto
Un **Atributo** es una propiedad atómica o característica que describe una [Entidad](Entidad.md). Representa la unidad mínima de información con significado que queremos almacenar.

*   **Tipología:** Pueden ser simples (ej. `Edad`), compuestos (ej. `Nombre Completo`) o multivaluados (ej. `Teléfonos`).
*   **Dominios:** Cada atributo tiene un conjunto de valores válidos (ej. un `Precio` debe ser numérico positivo).
*   **Identificación:** El atributo especial que distingue unívocamente a cada instancia es el Identificador (futura PK).

---

## 🗺️ Anclaje Visual (Dual Coding)
> [!abstract] Atributos en el Diagrama ER
> ```mermaid
> erDiagram
>     ENTIDAD {
>         string nombre_atributo
>         int id_pk PK
>     }
> ```

---

## 🔗 Conexiones y Contexto
*   **Se relaciona con:** [Entidad](Entidad.md) (a la que describe) y [Clave Primaria](Clave_Primaria.md) (el rol que asume el identificador).
*   **Diferencia clave con:** La **Entidad**, que tiene existencia autónoma; el atributo solo existe como parte de una entidad.

---

> [!tip] Idea Fuerza (Cierre)
> Si las entidades son sustantivos, los atributos son los adjetivos que les dan valor y detalle.
