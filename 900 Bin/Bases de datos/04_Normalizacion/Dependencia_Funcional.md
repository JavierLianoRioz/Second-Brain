---
tags: [concept, neuro-efficiency, normalization]
moc: "[00_MOC_Normalizacion](00_MOC_Normalizacion.md)"
status: refined
difficulty: intermediate
---

# Dependencia Funcional (DF)

---

## 🧠 Núcleo del Concepto

Una **Dependencia Funcional** (DF) es una restricción entre dos conjuntos de atributos en una relación. Se denota como $A \to B$, indicando que el valor de $A$ determina de manera única el valor de $B$.

*   **Determinación Única**: Si dos filas coinciden en el valor de $A$, obligatoriamente deben coincidir en el valor de $B$.
*   **Base de la Normalización**: Las formas normales se definen en función de qué tipos de DFs se permiten en una tabla.
*   **Identificador**: En una tabla bien diseñada, la Clave Primaria debe determinar funcionalmente a todos los demás atributos.

---

## 🗺️ Anclaje Visual (Dual Coding)

> [!abstract] Relación de Determinación
>
> ```mermaid
> graph LR
>     A[Atributo A] -- "determina a" --> B[Atributo B]
>     
>     subgraph "Ejemplo Real"
>     DNI[DNI] --> N[Nombre]
>     end
>     
>     style A fill:#f9f,stroke:#333
>     style DNI fill:#dfd,stroke:#333
> ```

---

## 🔗 Conexiones y Contexto

*   **Se relaciona con:** [Clave Primaria](../02_Dise%C3%B1o/Clave_Primaria.md) (es la DF principal).
*   **Impacto:**
    *   **DF Parcial**: Viola la [Segunda Forma Normal 2FN](Segunda_Forma_Normal_2FN.md).
    *   **DF Transitiva**: Viola la [Tercera Forma Normal 3FN](Tercera_Forma_Normal_3FN.md).

---

> [!tip] Idea Fuerza (Cierre)
> La Dependencia Funcional es el "ADN" de la tabla: define qué atributos están vinculados por su naturaleza y cuáles solo están juntos por accidente.

---

## 🗺️ Mapa de Contenido
*   Volver a: [00 MOC Normalización](00_MOC_Normalizacion.md).
