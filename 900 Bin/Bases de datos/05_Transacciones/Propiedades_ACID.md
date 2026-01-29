---
tags: [concept, neuro-efficiency, transactions]
moc: "[00_MOC_Transacciones](00_MOC_Transacciones.md)"
status: refined
difficulty: easy
---

# Propiedades ACID

---

## 🧠 Núcleo del Concepto

**ACID** es el acrónimo que define los cuatro requisitos fundamentales que garantizan que una transacción de base de datos sea fiable y segura.

*   **Atomicidad (Atomicity)**: La transacción es indivisible; si falla un solo paso, falla toda la operación.
*   **Consistencia (Consistency)**: Una transacción siempre lleva a la BD de un estado válido a otro, respetando todas las [restricciones](../03_SQL/Constraints_SQL.md).
*   **Aislamiento (Isolation)**: Las transacciones simultáneas se ejecutan como si fueran las únicas en el sistema (evita interferencias).
*   **Durabilidad (Durability)**: Una vez confirmado el cambio, este persiste incluso si hay un apagón o fallo del sistema.

---

## 🗺️ Anclaje Visual (Dual Coding)

> [!abstract] Los 4 Pilares de la Integridad
>
> ```mermaid
> graph TD
>     ACID[Propiedades ACID] --> A[Atomicidad: Todo o Nada]
>     ACID --> C[Consistencia: Estado Válido]
>     ACID --> I[Aislamiento: Sin Interferencias]
>     ACID --> D[Durabilidad: Permanencia]
>     
>     style ACID fill:#f9f,stroke:#333
> ```

---

## 🔗 Conexiones y Contexto

*   **Se aplica a:** [Transacción](Transacci%C3%B3n.md).
*   **Implementación:** Los motores de BD utilizan logs y bloqueos para garantizar estas propiedades.
*   **Contraste:** En sistemas distribuidos, a veces se prefiere el modelo *BASE* (Basic Availability, Soft state, Eventual consistency).

---

> [!tip] Idea Fuerza (Cierre)
> ACID es la "constitución" de la base de datos: garantiza que tus datos sean ley y no se pierdan en el caos del software.

---

## 🗺️ Mapa de Contenido
*   Volver a: [00 MOC Transacciones](00_MOC_Transacciones.md).
