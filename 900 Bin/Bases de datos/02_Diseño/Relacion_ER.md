---
tags: [concept, neuro-efficiency, db-design]
moc: "[00_MOC_Diseño](00_MOC_Diseño.md)"
status: refined
difficulty: intermediate
---

# Relación (ER)

---

## 🧠 Núcleo del Concepto
Una **Relación** define la asociación lógica entre dos o más entidades en el modelo de datos.

*   **Cardinalidad:** Determina el número máximo de instancias de una entidad que pueden estar asociadas con una instancia de otra (1:1, 1:N, N:M).
*   **Participación:** Indica si una entidad DEBE obligatoriamente estar relacionada con otra (total) o no (parcial).
*   **Grado:** Número de entidades que participan (binarias, ternarias, etc.).

---

## 🗺️ Anclaje Visual (Dual Coding)
> [!abstract] Tipos de Cardinalidad
> ```mermaid
> erDiagram
>     USUARIO ||--|| PERFIL : "1:1"
>     CLIENTE ||--o{ PEDIDO : "1:N"
>     ESTUDIANTE }|--|{ ASIGNATURA : "N:M"
> ```

---

## 💡 Práctica de Recuperación
> [!success]- Reto: Identifica la Cardinalidad
> **1. Gimnasio**: Un `Socio` asiste a muchas `Clases`, y una `Clase` tiene muchos `Socios`.
> **2. Hospital**: Un `Médico` atiende a muchos `Pacientes`, pero cada `Paciente` tiene un único médico asignado.
> 
> **Soluciones**:
> 1.  **N:M**. Implementada con tabla intermedia.
> 2.  **1:N**. La FK va en la tabla de Pacientes.

---

> [!tip] Idea Fuerza (Cierre)
> Las relaciones son los verbos de la base de datos: definen CÓMO interactúan los sujetos (entidades).
