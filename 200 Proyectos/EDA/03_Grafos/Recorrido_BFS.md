---
tags: [eda, algorithm, graphs, traversal]
---
# Recorrido en Anchura (BFS)

El **BFS** (*Breadth-First Search*) explora un grafo nivel por nivel, visitando todos los vecinos directos de un nodo antes de pasar a los nietos.

## Complejidad Big O

| Operación | Complejidad | Notas |
| :--- | :--- | :--- |
| **Inserción (Cola)** | $O(1)$ | Cada vértice se inserta y extrae una vez de la cola. |
| **Exploración** | $O(V + E)$ | Se visitan todos los vértices ($V$) y se exploran todas las aristas ($E$). |
| **Peek** | $O(1)$ | Consultar el siguiente nodo a visitar en la cola. |

## Mecanismo
1. Utiliza una **Cola** (FIFO).
2. Marca los nodos visitados para evitar ciclos.
3. Útil para encontrar el **camino más corto** en grafos no ponderados.

> [!example]+ Ejemplo Visual (Paso a Paso)
> Partiendo del nodo **A** en un grafo simple:
> ```mermaid
> graph TD
>     A((A)) --- B((B))
>     A --- C((C))
>     B --- D((D))
>     C --- E((E))
> ```
> **Orden de visita:**
> 1. Visitar **A** (Nivel 0)
> 2. Visitar **B**, **C** (Nivel 1)
> 3. Visitar **D**, **E** (Nivel 2)

---
[Regresar al MOC](00_MOC_Grafos.md)
