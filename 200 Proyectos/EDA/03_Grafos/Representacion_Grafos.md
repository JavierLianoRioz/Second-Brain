---
tags: [eda, data-structure, non-linear, graphs]
---

# Representación de Grafos

En informática, existen dos formas principales de representar un grafo en memoria. La elección depende de la **densidad** del grafo (relación entre vértices y aristas) y de las operaciones más frecuentes.

---

> [!abstract]+ 1. Matriz de Adyacencia
> Utiliza una **matriz bidimensional** (array de arrays) de tamaño $V \times V$.
> - `M[i][j] = 1`: Existe arista entre el nodo $i$ y el nodo $j$.
> - `M[i][j] = 0`: No existe arista.
>
> **Ventajas:** Rápido para verificar si dos nodos son adyacentes ($O(1)$).
> **Desventajas:** Consume mucha memoria ($O(V^2)$), ineficiente para grafos con pocas aristas (dispersos).
>
> **Ejemplo Visual:**
> ```mermaid
> graph LR
>     0 --- 1
>     0 --- 2
>     1 --- 2
> ```
> **Matriz Correspondiente:**
>
> | | 0 | 1 | 2 |
> | :---: | :---: | :---: | :---: |
> | **0** | 0 | 1 | 1 |
> | **1** | 1 | 0 | 1 |
> | **2** | 1 | 1 | 0 |
>
> **Código Java (Esquema):**
> ```java
> int[][] matriz = new int[V][V];
> // Añadir arista entre i y j
> matriz[i][j] = 1;
> matriz[j][i] = 1; // Si es no dirigido
> ```

> [!example]+ 2. Lista de Adyacencia
> Utiliza un **array de listas**. Cada índice $i$ del array contiene una lista de todos los nodos adyacentes al nodo $i$.
>
> **Ventajas:** Ahorra espacio en grafos dispersos ($O(V + E)$).
> **Desventajas:** Verificar si dos nodos son adyacentes es más lento ($O(V)$ en el peor caso).
>
> **Código Java (Basado en la Biblioteca):**
> ```java
> public class Graph {
>     private Node[] nodes; // Array de nodos
>
>     public void addEdge(int from, int to) {
>         Node nodeFrom = findNode(from);
>         Node nodeTo = findNode(to);
>         
>         if (nodeFrom != null && nodeTo != null) {
>             nodeFrom.addNeighbor(nodeTo); // Añade a la lista interna
>             nodeTo.addNeighbor(nodeFrom);
>         }
>     }
> }
> ```

---

## Comparativa de Complejidad

| Operación | Matriz de Adyacencia | Lista de Adyacencia |
| :--- | :--- | :--- |
| **Inserción (Arista)** | $O(1)$ | $O(1)$ |
| **Eliminación (Arista)** | $O(1)$ | $O(V)$ |
| **¿Son Adyacentes? (Peek)** | $O(1)$ | $O(V)$ |
| **Espacio Memoria** | $O(V^2)$ | $O(V + E)$ |

*(V = Vértices, E = Aristas)*

---
[Regresar al MOC](00_MOC_Grafos.md)
