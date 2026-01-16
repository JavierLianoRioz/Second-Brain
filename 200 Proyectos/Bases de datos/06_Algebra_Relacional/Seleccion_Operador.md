---
tags: [algebra-relacional, operator, theory]
moc: [[00_MOC_Algebra_Relacional]]
status: refined
difficulty: basic
---

# Selección (σ)

---

## 🧠 Núcleo del Concepto

El operador de **Selección** (σ) es una operación unaria que permite filtrar tuplas (filas) de una relación basándose en un predicado lógico.

*   **Entrada y Salida**: Toma una relación $R$ y devuelve otra relación con el mismo esquema, pero solo con las filas que cumplen la condición.
*   **Equivalencia SQL**: Se traduce directamente como la cláusula [[SQL_WHERE]].
*   **Conmutatividad**: $\sigma_a(\sigma_b(R)) = \sigma_b(\sigma_a(R)) = \sigma_{a \land b}(R)$.

---

## 🗺️ Representación

> [!abstract] Notación y Uso
> **Sintaxis**: $\sigma_{condición}(R)$
> 
> **Ejemplo**: Filtrar productos caros.
> $$\sigma_{precio > 100}(Productos)$$

---

## 🔗 Conexiones y Contexto

*   **Se relaciona con:** [[SQL_WHERE]], [[Algebra_Relacional_Concepto]].
*   **Diferencia clave con:** [[Proyeccion_Operador]], que filtra columnas en lugar de filas.

---

> [!tip] Idea Fuerza (Cierre)
> La selección es el "filtro vertical": te quedas con menos filas, pero con todas sus columnas intactas.
