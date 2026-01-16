---
tags: [concept, neuro-efficiency, db-design]
moc: [[00_MOC_Diseño]]
status: refactored
difficulty: intermediate
---

# Modelo Entidad-Relación (ER)

---

## 🧠 Núcleo del Concepto
El **Modelo Entidad-Relación (ER)** es el estándar para el diseño conceptual de bases de datos, permitiendo abstraer la realidad sin preocuparse por la implementación técnica.

*   **Entidades:** Objetos u conceptos del mundo real con existencia independiente.
*   **Atributos:** Propiedades que describen a las entidades.
*   **Relaciones:** Vínculos lógicos entre las entidades, definidos por su cardinalidad.

---

## 🗺️ Anclaje Visual (Dual Coding)
> [!abstract] Diagrama ER Básico
> ```mermaid
> erDiagram
>     CLIENTE ||--o{ PEDIDO : realiza
>     CLIENTE {
>         int id_cliente PK
>         string nombre
>     }
>     PEDIDO {
>         int id_pedido PK
>         date fecha
>     }
> ```

---

## 🔗 Conexiones y Contexto
*   **Se relaciona con:** [[Fases_del_Diseño_BD]] (es la herramienta de la fase conceptual) y [[Transformacion_ER_a_Relacional]] (su paso siguiente).
*   **Diferencia clave con:** **Modelo Relacional**, que es un modelo lógico basado en tablas, mientras que el ER es conceptual basado en diagramas.

---

> [!tip] Idea Fuerza (Cierre)
> El Modelo ER es el puente entre el lenguaje del negocio y la estructura técnica de los datos.
