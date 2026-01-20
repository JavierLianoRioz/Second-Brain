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

> [!example]+ Rotación Simple a la Izquierda (RR)
> Ocurre cuando insertamos en la derecha del hijo derecho.
> ```mermaid
> graph TD
>     A((1)) --- B((2))
>     B --- C((3))
>     style A fill:#f96,stroke:#333
>     style B fill:#f96,stroke:#333
>     style C fill:#9f9,stroke:#333
> ```
> **Resultado:**
> ```mermaid
> graph TD
>     B((2)) --- A((1))
>     B --- C((3))
>     style B fill:#9f9,stroke:#333
> ```

> [!example]+ Rotación Simple a la Derecha (LL)
> Ocurre cuando insertamos en la izquierda del hijo izquierdo.
> ```mermaid
> graph TD
>     C((3)) --- B((2))
>     B --- A((1))
>     style C fill:#f96,stroke:#333
>     style B fill:#f96,stroke:#333
>     style A fill:#9f9,stroke:#333
> ```
> **Resultado:**
> ```mermaid
> graph TD
>     B((2)) --- A((1))
>     B --- C((3))
>     style B fill:#9f9,stroke:#333
> ```

> [!example]+ Rotación Doble IZQ-DER (LR)
> Desequilibrio en "zigzag": izquierda y luego derecha.
> **Paso 1: Rotación simple a la izquierda sobre el hijo (1)**
> ```mermaid
> graph TD
>     C((3)) --- A((1))
>     A --- B((2))
>     style C fill:#f96,stroke:#333
>     style A fill:#f96,stroke:#333
>     style B fill:#9f9,stroke:#333
> ```
> **Paso 2: Rotación simple a la derecha sobre la raíz (3)**
> ```mermaid
> graph TD
>     C((3)) --- B((2))
>     B --- A((1))
> ```
> **Resultado Final:**
> ```mermaid
> graph TD
>     B((2)) --- A((1))
>     B --- C((3))
>     style B fill:#9f9,stroke:#333
> ```

> [!example]+ Rotación Doble DER-IZQ (RL)
> Desequilibrio en "zigzag": derecha y luego izquierda.
> **Paso 1: Rotación simple a la derecha sobre el hijo (3)**
> ```mermaid
> graph TD
>     A((1)) --- C((3))
>     C --- B((2))
>     style A fill:#f96,stroke:#333
>     style C fill:#f96,stroke:#333
>     style B fill:#9f9,stroke:#333
> ```
> **Paso 2: Rotación simple a la izquierda sobre la raíz (1)**
> ```mermaid
> graph TD
>     A((1)) --- B((2))
>     B --- C((3))
> ```
> **Resultado Final:**
> ```mermaid
> graph TD
>     B((2)) --- A((1))
>     B --- C((3))
>     style B fill:#9f9,stroke:#333
> ```

## Complejidad Big O

Al estar siempre balanceado, el AVL evita el peor caso de $O(n)$ de los BST normales.

| Operación       | Complejidad Promedio | Complejidad Peor Caso |
| :-------------- | :------------------- | :-------------------- |
| **Inserción**   | $O(\log n)$          | $O(\log n)$           |
| **Edición**     | $O(\log n)$          | $O(\log n)$           |
| **Eliminación** | $O(\log n)$          | $O(\log n)$           |
| **Peek**        | $O(\log n)$          | $O(\log n)$           |

---
[Regresar al MOC](00_MOC_Arboles.md)
