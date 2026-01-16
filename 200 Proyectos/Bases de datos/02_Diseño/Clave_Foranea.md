---
tags: [concept, neuro-efficiency, db-design]
moc: [[00_MOC_Diseño]]
status: refactored
difficulty: easy
---

# Clave Foránea (FK)

---

## 🧠 Núcleo del Concepto
La **Clave Foránea (FK)** es un atributo en una tabla que apunta a la [Clave Primaria](Clave_Primaria.md) de otra, estableciendo un vínculo lógico entre ambas.

*   **Integridad Referencial:** Garantiza que no existan valores en la FK que no existan previamente en la tabla referenciada (excepto `NULL` si la lógica lo permite).
*   **Navegación:** Es el "puntero" que permite realizar JOINs y reconstruir la información fragmentada por la normalización.
*   **Acciones en Cascada:** Permite definir qué sucede al borrar o actualizar (ej. `ON DELETE CASCADE`).

---

## 🗺️ Anclaje Visual (Dual Coding)
> [!abstract] El Vínculo entre Tablas
> ```mermaid
> erDiagram
>     PEDIDO }o--|| CLIENTE : "id_cliente (FK) -> id_cliente (PK)"
> ```

---

## 🔗 Conexiones y Contexto
*   **Se relaciona con:** [[Clave_Primaria]] (su destino) y [[Relacion_ER]] (la FK es la implementación física de una relación).
*   **Diferencia clave con:** **Clave Primaria**, que identifica a la fila local, mientras que la FK vincula con una fila externa.

---

> [!tip] Idea Fuerza (Cierre)
> Las FKs son el pegamento del modelo relacional; sin ellas, tendríamos tablas aisladas sin sentido de conjunto.
