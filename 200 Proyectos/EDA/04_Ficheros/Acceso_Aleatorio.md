---
tags: [eda, files, persistence]
---
# Acceso Aleatorio (Directo)

El **Acceso Aleatorio** permite acceder a cualquier registro de un fichero de forma directa, sin tener que pasar por los registros anteriores, utilizando su posición o dirección física.

## Complejidad Big O

Para que sea $O(1)$, los registros deben tener un **tamaño fijo**.

| Operación | Complejidad | Notas |
| :--- | :--- | :--- |
| **Inserción** | $O(1)$ | Si se conoce la posición libre. |
| **Edición** | $O(1)$ | Conociendo la dirección (seek) y con registros de tamaño fijo. |
| **Eliminación** | $O(1)$ / $O(n)$ | $O(1)$ para borrado lógico. $O(n)$ si se compacta el fichero. |
| **Peek (Índice)** | $O(1)$ | Cálculo directo de posición: `offset = index * recordSize`. |

## Características
- Permite saltar directamente a cualquier posición (`seek`).
- Requiere registros de longitud fija para calcular el desplazamiento.
- Ejemplo físico: Disco duro o CD-ROM.

---
[Regresar al MOC](00_MOC_Ficheros.md)
