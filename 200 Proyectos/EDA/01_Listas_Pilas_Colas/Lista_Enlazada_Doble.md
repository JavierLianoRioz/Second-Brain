---
tags: [eda, data-structure, linear]
---

# Lista Enlazada Doble (Doubly Linked List)

A diferencia de la simple, cada nodo contiene un puntero al **anterior** y al **siguiente**.

## Complejidad Big O

| Operación       | Complejidad | Notas                                                                  |
| :-------------- | :---------- | :--------------------------------------------------------------------- |
| **Inserción**   | $O(1)$      | Si se tiene referencia al nodo tail, la inserción al final es $O(1)$.  |
| **Edición**     | $O(n)$      | Búsqueda bidireccional no reduce la complejidad asintótica.            |
| **Eliminación** | $O(1)$      | Si se conoce el nodo, no requiere recorrer para encontrar el anterior. |
| **Peek**        | $O(n)$      | Acceso por índice (requiere recorrido).                                |

---
[Regresar al MOC](00_MOC_Lineales.md)
