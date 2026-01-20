---
tags: [eda, data-structure, non-linear, trees]
---

# Árbol Binario (Binary Tree)

Un **Árbol Binario** es una estructura jerárquica donde cada nodo tiene como máximo dos hijos, referenciados comúnmente como hijo izquierdo e hijo derecho.

## Complejidad Big O

A diferencia de los árboles de búsqueda (BST), un árbol binario genérico no mantiene un orden específico, lo que afecta a las operaciones de búsqueda y edición.

| Operación | Complejidad | Notas |
| :--- | :--- | :--- |
| **Inserción** | $O(n)$ | Sin orden, requiere buscar un hueco libre (usualmente por niveles). |
| **Edición** | $O(n)$ | Requiere búsqueda exhaustiva (recorrido completo en el peor caso). |
| **Eliminación** | $O(n)$ | Requiere encontrar el nodo y reestructurar si es necesario. |
| **Peek (Búsqueda)** | $O(n)$ | Sin orden, se debe recorrer todo el árbol ($O(n)$). |

---
[Regresar al MOC](00_MOC_Arboles.md)
