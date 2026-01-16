---
tags: [concept, neuro-efficiency, sql, transactions]
moc: "[00_MOC_Transacciones](00_MOC_Transacciones.md)"
status: refined
difficulty: intermediate
---

# Comandos de Control de Transacciones (TCL)

---

## 🧠 Núcleo del Concepto

Los comandos **TCL** (Transaction Control Language) son palabras clave de SQL que permiten gestionar el inicio, la finalización y los puntos intermedios de una [Transacción](Transacci%C3%B3n.md).

*   **`START TRANSACTION` / `BEGIN`**: Marca el inicio del bloque atómico.
*   **`COMMIT`**: Confirma y guarda permanentemente todos los cambios realizados desde el inicio.
*   **`ROLLBACK`**: Anula todos los cambios y devuelve la base de datos al estado previo al inicio.
*   **`SAVEPOINT`**: Establece "puntos de restauración" internos dentro de una transacción larga.

---

## 🗺️ Anclaje Visual (Dual Coding)

> [!abstract] Control de Flujo TCL
>
> ```mermaid
> graph LR
>     B[BEGIN] --> D[Operaciones DML]
>     D --> S{¿Todo OK?}
>     S -- Sí --> C[COMMIT]
>     S -- No --> R[ROLLBACK]
>     
>     style B fill:#dfd,stroke:#333
>     style C fill:#ccf,stroke:#333
>     style R fill:#fdd,stroke:#333
> ```

---

## 🔗 Conexiones y Contexto

*   **Parte de:** Las sub-áreas de SQL ([SQL DML](../03_SQL/SQL_DML.md)).
*   **Garantiza:** Las [Propiedades ACID](Propiedades_ACID.md), especialmente la Atomicidad.
*   **Práctica**: [Transacciones Control](../08_Programacion_BD/Transacciones_Control.md).

---

> [!tip] Idea Fuerza (Cierre)
> TCL es tu "seguro de vida" en SQL: te permite cometer errores en memoria y arrepentirte antes de que afecten a la realidad del disco.

---

## 🗺️ Mapa de Contenido
*   Volver a: [00 MOC Transacciones](00_MOC_Transacciones.md).
