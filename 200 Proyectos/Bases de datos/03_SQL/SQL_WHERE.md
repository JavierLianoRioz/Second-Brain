---
tags: [sql, dml, database]
moc: "[00_MOC_SQL](00_MOC_SQL.md)"
status: refined
difficulty: intermediate
---

# SQL WHERE: Filtrado de Datos

---

## 🧠 Núcleo del Concepto

La cláusula **WHERE** se utiliza para filtrar los registros de una consulta basándose en una o más condiciones específicas. Solo las filas que cumplen la condición son procesadas por el comando principal.

*   **Ubicación**: Se aplica después del `FROM` y antes del `GROUP BY` u `ORDER BY`.
*   **Versatilidad**: Funciona con [SELECT Basico](SELECT_Basico.md), [UPDATE](UPDATE.md) y [DELETE](DELETE.md).
*   **Lógica Booleana**: Permite combinar múltiples filtros usando `AND`, `OR` y `NOT`.

---

## 💻 Operadores Comunes

| Tipo | Operadores | Uso |
| :--- | :--- | :--- |
| **Comparación** | `=`, `<>`, `>`, `<`, `>=`, `<=` | Valores exactos o rangos. |
| **Conjuntos** | `IN (v1, v2, ...)` | Coincidencia con cualquier valor de la lista. |
| **Rangos** | `BETWEEN min AND max` | Valores dentro de un intervalo inclusivo. |
| **Patrones** | `LIKE 'texto%'` | Búsqueda parcial (comodín `%`). |
| **Nulos** | `IS NULL` / `IS NOT NULL` | Tratamiento de valores ausentes. |

---

## 🗺️ Anclaje Visual (Dual Coding)

> [!abstract] El Embudo de Datos
> 
> ```mermaid
> graph TD
>     T[(Tabla Completa)] --> F{Cláusula WHERE}
>     F -->|Cumple| R[Fila en Resultado]
>     F -->|No cumple| D[Fila Descartada]
>     
>     style F fill:#f96,stroke:#333
> ```

---

## 🔗 Conexiones y Contexto

*   **Equivalencia Teórica:** Es la implementación directa del operador de **Selección (σ)** del [Algebra Relacional Concepto](../06_Algebra_Relacional/Algebra_Relacional_Concepto.md).
*   **Optimizador:** El uso de índices en columnas dentro del `WHERE` es crítico para la [Query Optimization](../07_Optimizacion/Query_Optimization.md).

---

> [!tip] Idea Fuerza (Cierre)
> Sin un `WHERE`, estás hablando con toda la tabla; con un `WHERE`, estás interrogando solo a los culpables.

---

## 🗺️ Mapa de Contenido
*   Volver a: [SELECT Basico](SELECT_Basico.md) o [00 MOC SQL](00_MOC_SQL.md).
