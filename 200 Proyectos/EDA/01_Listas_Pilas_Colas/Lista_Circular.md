---
tags: [eda, data-structure, linear]
---

# Lista Circular (Circular Linked List)

En una **Lista Circular**, el último nodo no apunta a `null`, sino que apunta de nuevo al primer nodo (head), formando un ciclo.

## Complejidad Big O

| Operación | Complejidad | Notas |
| :--- | :--- | :--- |
| **Inserción** | $O(1)$ | Si se mantiene un puntero al último nodo (`tail`), la inserción al inicio o final es $O(1)$. |
| **Edición** | $O(n)$ | Requiere recorrido secuencial. |
| **Eliminación** | $O(1)$ | $O(1)$ para el inicio si hay `tail`. $O(n)$ para el final. |
| **Peek** | $O(n)$ | Acceso por índice. |

## Casos de Uso
- Gestión de turnos (Round Robin).
- Buffers circulares.

---
[Regresar al MOC](00_MOC_Lineales.md)
