---
tags: [concept, neuro-efficiency, db-design]
moc: "[00_MOC_Diseño](00_MOC_Diseño.md)"
status: refined
difficulty: easy
---

# Fases del Diseño de Bases de Datos

---

## 🧠 Núcleo del Concepto
El diseño de una base de datos es un flujo estructurado que garantiza que la implementación técnica responda exactamente a la necesidad del negocio.

*   **Fase Conceptual:** Abstracción de la realidad mediante diagramas independientes de la tecnología (Herramienta: [Modelo Entidad-Relación](Modelo_Entidad_Relacion.md)).
*   **Fase Lógica:** Traducción del diagrama conceptual a un modelo de datos específico (Herramienta: [Modelo Relacional Conceptos](Modelo_Relacional_Conceptos.md)).
*   **Fase Física:** Implementación real en un motor de base de datos concreto (MySQL, Oracle, etc.).

---

## 🗺️ Anclaje Visual (Dual Coding)
> [!abstract] El Embudo del Diseño
> ```mermaid
> graph TD
>     A[Requerimientos] --> B[Diseño Conceptual]
>     B --> C[Diseño Lógico]
>     C --> D[Diseño Físico]
>     style A fill:#f9f,stroke:#333
>     style D fill:#bbf,stroke:#333
> ```

---

## 🔗 Conexiones y Contexto
*   **Se relaciona con:** [SQL DDL](../03_SQL/SQL_DDL.md) (donde se ejecuta la fase física) y [Normalización Objetivos](../04_Normalizacion/Normalizacion_Objetivos.md) (parte de la fase de refinamiento lógico).
*   **Punto Crítico:** Un error en la fase conceptual suele costar 10 veces más de corregir si se detecta en la fase física.

---

> [!tip] Idea Fuerza (Cierre)
> No se construye una casa sin planos; no se genera una base de datos sin diseño conceptual y lógico previo.
