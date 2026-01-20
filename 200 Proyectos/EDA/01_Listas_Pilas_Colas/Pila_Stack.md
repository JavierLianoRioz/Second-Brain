---
tags: [eda, data-structure, linear, adt]
---

# Pila (Stack)

Una **Pila** es un ADT (Tipo de Dato Abstracto) que sigue el principio **LIFO** (*Last In, First Out*). El último en entrar es el primero en salir.

## Complejidad Big O

| Operación | Complejidad | Nombre Común |
| :--- | :--- | :--- |
| **Inserción** | $O(1)$ | `push()` |
| **Edición** | $O(n)$ | No es común (normalmente solo se accede al tope). |
| **Eliminación** | $O(1)$ | `pop()` |
| **Peek** | $O(1)$ | `top()` o `peek()` |

---
[Regresar al MOC](00_MOC_Lineales.md)
