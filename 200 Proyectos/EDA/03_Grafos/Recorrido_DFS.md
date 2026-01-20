---
tags: [eda, algorithm, graphs, traversal]
---
# Recorrido en Profundidad (DFS)

El **DFS** (*Depth-First Search*) explora un grafo siguiendo una rama hasta el final antes de retroceder (backtracking).

## Complejidad Big O

| Operación | Complejidad | Notas |
| :--- | :--- | :--- |
| **Inserción (Pila)** | $O(1)$ | Cada vértice se apila y desapila una vez. |
| **Exploración** | $O(V + E)$ | Igual que BFS, visita todos los nodos y aristas. |
| **Peek** | $O(1)$ | Consultar el tope de la pila. |

## Mecanismo
1. Utiliza una **Pila** (LIFO) o **Recursión**.
2. Explora lo más profundo posible antes de retroceder.
3. Útil para detectar ciclos, ordenación topológica y componentes conexas.

> [!example]+ Ejemplo Visual (Paso a Paso)
> Partiendo del nodo **A**:
> ```mermaid
> graph TD
>     A((A)) --- B((B))
>     B --- D((D))
>     A --- C((C))
>     C --- E((E))
> ```
> **Orden de visita (posible):**
> 1. Visitar **A**
> 2. Ir profundo a **B**
> 3. Ir profundo a **D**
> 4. Retroceder a **A** e ir a **C**
> 5. Ir profundo a **E**

---
[Regresar al MOC](00_MOC_Grafos.md)
