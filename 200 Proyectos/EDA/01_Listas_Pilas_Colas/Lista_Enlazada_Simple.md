---
tags: [eda, data-structure, linear]
---

# Lista Enlazada Simple (Singly Linked List)

Una **Lista Enlazada Simple** es una estructura de datos lineal compuesta por nodos donde cada uno contiene un valor y una referencia (puntero) al siguiente nodo de la secuencia.

```java
Nodo () {
	Nodo siguiente;
	ó
	Nodo anterior;
}

```

Usuario -> Madre -> Nodo -> Nodo -> Nodo -> Nodo
Usuario -> Madre -> 1 -> 2 -> 3 -> 4
## Complejidad Big O

| Operación       | Complejidad | Notas                                                         |
| :-------------- | :---------- | :------------------------------------------------------------ |
| **Inserción**   | $O(1)$      | En el frente. $O(n)$ si es en el final o posición específica. |
| **Edición**     | $O(n)$      | Requiere búsqueda del elemento.                               |
| **Eliminación** | $O(1)$      | En el frente. $O(n)$ si es en el final o posición específica. |
| **Peek**        | $O(n)$      | Acceso por índice (requiere recorrido secuencial).            |

## Atributos
- **Nodo Head**: Puntero al primer elemento.
- **Acceso Secuencial**: No permite acceso aleatorio (como los arrays).

---
[Regresar al MOC](00_MOC_Lineales.md)
