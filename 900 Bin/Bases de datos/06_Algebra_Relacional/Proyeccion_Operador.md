---
tags: [theory, relational-algebra, database]
moc: "[00_MOC_Algebra_Relacional](00_MOC_Algebra_Relacional.md)"
status: refined
difficulty: intermediate
---

# Proyección (π)

---

## 🧠 Núcleo del Concepto

El operador de **Proyección** (π) es una operación unaria que permite seleccionar un subconjunto de atributos (columnas) de una relación, descartando el resto.

*   **Eliminación de Duplicados**: Por definición matemática, la proyección elimina filas duplicadas si al quitar columnas algunas tuplas resultan idénticas.
*   **Equivalencia SQL**: Se corresponde con la lista de campos en la cláusula [SQL SELECT](../03_SQL/SELECT_Basico.md) (nombre técnico en SQL).
*   **Cascada**: $\pi\{L1\}(\pi\{L2\}(R)) = \pi\{L1\}(R)$ siempre que $L1 \subseteq L2$.

---

## 🗺️ Representación

> [!abstract] Notación y Uso
> **Sintaxis**: $\pi\{Atributos\}(R)$
> 
> **Ejemplo**: Obtener lista de precios.
> $$\pi\{nombre, precio\}(Productos)$$

---

## 🔗 Conexiones y Contexto

*   **Se relaciona con:** [SQL SELECT](../03_SQL/SELECT_Basico.md), [Algebra Relacional Concepto](Algebra_Relacional_Concepto.md).
*   **Diferencia clave con:** [Seleccion Operador](Seleccion_Operador.md), que filtra filas; la proyección filtra el "ancho" de la tabla.

---

> [!tip] Idea Fuerza (Cierre)
> La proyección es el "tijeretazo horizontal": eliges qué columnas quieres ver, ignorando las demás.
---

## 🗺️ Mapa de Contenido
*   Volver a: [00 MOC Algebra Relacional](00_MOC_Algebra_Relacional.md).
