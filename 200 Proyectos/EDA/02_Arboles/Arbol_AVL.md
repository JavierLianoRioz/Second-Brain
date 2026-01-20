---
tags: [eda, data-structure, non-linear, trees]
---

# Árbol AVL

El **Árbol AVL** (Adelson-Velsky y Landis) es un [[Arbol_Binario_Busqueda_BST|Árbol Binario de Búsqueda (BST)]] **auto-balanceable**. Su característica principal es que mantiene una altura optimizada para garantizar operaciones en tiempo logarítmico.

## Factor de Equilibrio (FE)
Para cada nodo, el FE se calcula como la diferencia de alturas entre sus hijos:
$$FE = Altura(Hijo\_Derecho) - Altura(Hijo\_Izquierdo)$$
Un nodo se considera equilibrado si su $FE \in \{-1, 0, 1\}$.

## Mecanismo de Balanceo: Rotaciones
Cuando una inserción o eliminación provoca que $|FE| > 1$, se deben realizar rotaciones para reequilibrar el árbol:

1. **Rotación Simple (LL / RR)**: Se aplica cuando el desequilibrio es lineal (un hijo y su nieto están en la misma dirección).
2. **Rotación Doble (LR / RL)**: Se aplica cuando el desequilibrio forma un "zigzag". Primero se endereza la rama con una rotación simple y luego se aplica la rotación principal.

## Complejidad Big O

Al estar siempre balanceado, el AVL evita el peor caso de $O(n)$ de los BST normales.

| Operación | Complejidad Promedio | Complejidad Peor Caso |
| :--- | :--- | :--- |
| **Inserción** | $O(\log n)$ | $O(\log n)$ |
| **Edición** | $O(\log n)$ | $O(\log n)$ |
| **Eliminación** | $O(\log n)$ | $O(\log n)$ |
| **Peek** | $O(\log n)$ | $O(\log n)$ |

---
[Regresar al MOC](00_MOC_Arboles.md)
