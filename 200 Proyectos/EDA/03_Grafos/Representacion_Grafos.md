---
tags: [eda, data-structure, non-linear, graphs]
---

# Representación de Grafos

Los grafos se pueden representar principalmente de dos formas: **Matriz de Adyacencia** y **Lista de Adyacencia**.

## Complejidad Big O (Comparativa)

| Operación | Matriz de Adyacencia | Lista de Adyacencia |
| :--- | :--- | :--- |
| **Inserción (Arista)** | $O(1)$ | $O(1)$ |
| **Eliminación (Arista)** | $O(1)$ | $O(V)$ o $O(E)$ (depende de la implementación) |
| **¿Son Adyacentes? (Peek)** | $O(1)$ | $O(V)$ |
| **Espacio Memoria** | $O(V^2)$ | $O(V + E)$ |

*(V = Vértices, E = Aristas)*

---
[Regresar al MOC](00_MOC_Grafos.md)
