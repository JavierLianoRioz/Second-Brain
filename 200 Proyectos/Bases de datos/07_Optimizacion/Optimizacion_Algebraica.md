---
tags: [optimization, relational-algebra, theory]
moc: [[00_MOC_Optimizacion]]
status: original
difficulty: advanced
---

# Optimización Algebraica: Selecciones Tempranas

---

## 🧠 Núcleo del Concepto

En optimización de consultas, "mover el join" (o más técnicamente, **Pushing Selections Down**) consiste en aplicar los filtros ($\sigma$) lo más cerca posible de las fuentes de datos, *antes* de realizar operaciones costosas como el Join ($\bowtie$).

*   **El Problema**: Hacer un Join de dos tablas completas genera un volumen de datos enorme en memoria antes de ser filtrado.
*   **La Solución**: Filtrar las filas de cada tabla por separado y luego unir solo los resultados.
*   **Regla de Oro**: Siempre que una condición de filtrado solo afecte a una de las tablas, muévela debajo del Join en el árbol de la consulta.

---

## 🗺️ Anclaje Visual (Dual Coding)

> [!abstract] De Árbol Ineficiente a Árbol Optimizado
> 
> ```mermaid
> graph TD
>     subgraph "Ineficiente: σ{R.id=5}(R ⨝ S)"
>     A1[Resultado] --- B1["Selección (σ{R.id=5})"]
>     B1 --- C1["JOIN (⨝)"]
>     C1 --- D1[Relación R]
>     C1 --- E1[Relación S]
>     end
> 
>     subgraph "Optimizado: σ{R.id=5}(R) ⨝ S"
>     A2[Resultado] --- C2["JOIN (⨝)"]
>     C2 --- B2["Selección (σ{R.id=5})"]
>     C2 --- E2[Relación S]
>     B2 --- D2[Relación R]
>     end
> ```

---

## 📝 Ejemplo de Transformación

Imagina que quieres los pedidos del cliente con `ID=5`.

### 1. Fórmula Ineficiente
$$\sigma\{id=5\}(Clientes \bowtie Pedidos)$$
*   **Qué hace**: Une todos los clientes con todos los pedidos (millones de filas) y *luego* busca al número 5.

### 2. Fórmula Optimizada
$$\sigma\{id=5\}(Clientes) \bowtie Pedidos$$
*   **Qué hace**: Busca al cliente 5 (1 sola fila) y une esa única fila con sus pedidos correspondientes. **El ahorro de CPU y RAM es masivo.**

---

## 🔗 Conexiones y Contexto

*   **Se basa en:** [Join Algebra](Join_Algebra.md) y [Seleccion Operador](Seleccion_Operador.md).
*   **Equivalencia SQL:** El [Query Optimization](Query_Optimization.md) hace esto automáticamente cuando escribes un `WHERE`.

---

> [!tip] Idea Fuerza (Cierre)
> Optimizar es como lavar la fruta antes de cocinarla: no quieres meter suciedad (filas innecesarias) en la olla (el Join).

---

## 📝 Ejercicio Rápido de Examen
**Pregunta**: Optimiza la siguiente expresión: $\sigma\{R.A=10 \land S.B>100\}(R \bowtie S)$
**Respuesta**: $\sigma\{A=10\}(R) \bowtie \sigma\{B>100\}(S)$
