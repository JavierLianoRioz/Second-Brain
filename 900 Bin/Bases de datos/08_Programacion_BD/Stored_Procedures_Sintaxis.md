---
tags: [concept, neuro-efficiency, db-programming]
moc: "[00_MOC_Programacion_BD](00_MOC_Programacion_BD.md)"
status: refined
difficulty: intermediate
---

# Sintaxis de Stored Procedures

---

## 🧠 Núcleo del Concepto
Un **Stored Procedure** es un bloque de código SQL precompilado que reside en el servidor, permitiendo ejecutar múltiples operaciones bajo una única interfaz de llamada.

*   **Parámetros:** Utiliza modificadores `IN` (entrada), `OUT` (salida) o `INOUT` (ambos) para intercambiar datos.
*   **Encapsulamiento:** La lógica interna es transparente para el cliente, mejorando la seguridad y mantenibilidad.
*   **Delimitadores:** Requiere cambiar el terminador SQL (ej. `//`) para permitir el uso de `;` dentro del cuerpo del procedimiento.

---

## 🗺️ Anclaje Visual (Dual Coding)
> [!abstract] Flujo de Creación y Ejecución
> ```mermaid
> sequenceDiagram
>     participant U as Usuario/App
>     participant S as Servidor BD
>     Note over S: DELIMITER //
>     U->>S: CREATE PROCEDURE...
>     Note over S: DELIMITER ;
>     U->>S: CALL procedimiento()
>     S-->>U: Resultado / Param OUT
> ```

---

## 🔗 Conexiones y Contexto
*   **Se relaciona con:** [Control de Flujo](Control_de_Flujo.md) (la lógica interna) y [Transacciones Control](Transacciones_Control.md) (para asegurar atomicidad en el procedimiento).
*   **Diferencia clave con:** **Funciones (UDF)**, las cuales deben devolver un valor y se usan dentro de expresiones SQL, mientras que los procedimientos se ejecutan con `CALL`.

---

> [!tip] Idea Fuerza (Cierre)
> Los Procedimientos Almacenados son la "API interna" de tu base de datos; ocultan la complejidad y exponen funcionalidad pura.
