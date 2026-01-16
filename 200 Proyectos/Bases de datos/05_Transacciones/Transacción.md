---
tags: [concept, neuro-efficiency, transactions]
moc: "[00_MOC_Transacciones](00_MOC_Transacciones.md)"
status: refined
difficulty: easy
---

# Transacción

---

## 🧠 Núcleo del Concepto

Una **Transacción** es una unidad lógica de trabajo que comprende una secuencia de operaciones de base de datos (generalmente [SQL DML](../03_SQL/SQL_DML.md)) que deben ejecutarse de forma atómica.

*   **Principio Todo o Nada**: O todas las operaciones se confirman con éxito o ninguna surte efecto en la base de datos.
*   **Puntos de Control**: Se consolidan mediante `COMMIT` para guardar permanentemente o `ROLLBACK` para revertir al estado inicial.
*   **Objetivo**: Mantener la integridad y consistencia de los datos ante fallos del sistema o concurrencia.

---

## 🗺️ Anclaje Visual (Dual Coding)

> [!abstract] El Ciclo de Vida de una Transacción
>
> ```mermaid
> stateDiagram-v2
>     [*] --> Activa
>     Activa --> Commit: Éxito total
>     Activa --> Rollback: Error / Fallo
>     Commit --> [*]: Datos persistidos
>     Rollback --> [*]: Estado restaurado
> ```

---

## 🔗 Conexiones y Contexto

*   **Fundamento**: Se rige por las [Propiedades ACID](Propiedades_ACID.md).
*   **Gestión**: Se controla mediante los [Comandos TCL](Comandos_TCL.md).
*   **Práctica**: Implementación en [SQL Procedural](../08_Programacion_BD/Transacciones_Control.md).

---

> [!tip] Idea Fuerza (Cierre)
> Una transacción es un "pacto de honor" con la base de datos: o se cumple la palabra completa o se olvida que alguna vez se dijo algo.

---

## 🗺️ Mapa de Contenido
*   Volver a: [00 MOC Transacciones](00_MOC_Transacciones.md).
