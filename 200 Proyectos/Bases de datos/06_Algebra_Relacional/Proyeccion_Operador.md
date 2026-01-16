---
tags: [algebra-relacional, operator, theory]
moc: [[00_MOC_Algebra_Relacional]]
status: refined
difficulty: basic
---

# Proyección (π)

---

## 🧠 Núcleo del Concepto

El operador de **Proyección** (π) es una operación unaria que permite seleccionar un subconjunto de atributos (columnas) de una relación, descartando el resto.

*   **Eliminación de Duplicados**: Por definición matemática, la proyección elimina filas duplicadas si al quitar columnas algunas tuplas resultan idénticas.
*   **Equivalencia SQL**: Se corresponde con la lista de campos en la cláusula [[SQL_SELECT]].
*   **Cascada**: $\pi_{L1}(\pi_{L2}(R)) = \pi_{L1}(R)$ siempre que $L1 \subseteq L2$.

---

## 🗺️ Representación

> [!abstract] Notación y Uso
> **Sintaxis**: $\pi_{Atributos}(R)$
> 
> **Ejemplo**: Obtener lista de precios.
> $$\pi_{nombre, precio}(Productos)$$

---

## 🔗 Conexiones y Contexto

*   **Se relaciona con:** [[SQL_SELECT]], [[Algebra_Relacional_Concepto]].
*   **Diferencia clave con:** [[Seleccion_Operador]], que filtra filas; la proyección filtra el "ancho" de la tabla.

---

> [!tip] Idea Fuerza (Cierre)
> La proyección es el "tijeretazo horizontal": eliges qué columnas quieres ver, ignorando las demás.
