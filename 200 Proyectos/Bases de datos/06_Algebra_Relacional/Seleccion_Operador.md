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
*   **Equivalencia SQL**: Se traduce directamente como la cláusula [SQL WHERE](../03_SQL/SQL_WHERE.md).
*   **Conmutatividad**: $\sigma\{a\}(\sigma\{b\}(R)) = \sigma\{b\}(\sigma\{a\}(R)) = \sigma\{a \land b\}(R)$.

---

## 🗺️ Representación

> [!abstract] Notación y Uso
> **Sintaxis**: $\sigma\{condición\}(R)$
> 
> **Ejemplo**: Filtrar productos caros.
> $$\sigma\{precio > 100\}(Productos)$$

---

## 🔗 Conexiones y Contexto

*   **Se relaciona con:** [SQL WHERE](../03_SQL/SQL_WHERE.md), [Algebra Relacional Concepto](Algebra_Relacional_Concepto.md).
*   **Diferencia clave con:** [Proyeccion Operador](Proyeccion_Operador.md), que filtra columnas en lugar de filas.

---

> [!tip] Idea Fuerza (Cierre)
> La selección es el "filtro vertical": te quedas con menos filas, pero con todas sus columnas intactas.
---

## 🗺️ Mapa de Contenido
*   Volver a: [00 MOC Algebra Relacional](00_MOC_Algebra_Relacional.md).
