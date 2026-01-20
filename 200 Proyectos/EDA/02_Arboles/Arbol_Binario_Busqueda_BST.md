---
tags: [eda, data-structure, non-linear, trees]
---
# Árbol Binario de Búsqueda (BST)

Un **BST** es un árbol binario donde para cada nodo, los valores a la izquierda son menores y a la derecha son mayores.

```
class Arbol(): Menu {
	Nodo raiz;
	
	insertar(Nodo unNodo);
	editar(int posicion, Nodo unNodo);
	eliminar(int posicion);
	peek(int posicion): Nodo;
	
	int numeroNodos;
}

class Nodo(): Comidas {
	Nodo hijoIzquierdo; < calorias
	Nodo hijoDerecho; > calorias
	
	int calorias;
}
```

## Complejidad Big O

| Operación       | Complejidad Promedio | Complejidad Peor Caso |
| :-------------- | :------------------- | :-------------------- |
| **Inserción**   | $O(\log n)$          | $O(n)$                |
| **Edición**     | $O(\log n)$          | $O(n)$                |
| **Eliminación** | $O(\log n)$          | $O(n)$                |
| **Peek**        | $O(\log n)$          | $O(n)$                |

> [!NOTE]
> El peor caso ocurre cuando el árbol no está balanceado.

---
[Regresar al MOC](00_MOC_Arboles.md)
