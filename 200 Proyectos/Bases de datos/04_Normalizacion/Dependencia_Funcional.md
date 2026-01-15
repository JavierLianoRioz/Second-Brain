# Dependencia Funcional

Una **Dependencia Funcional (DF)** describe la relación entre atributos.
Se denota `A -> B` (A determina a B).

*   Significa que si conocemos el valor de `A`, podemos determinar el valor único de `B`.

## Ejemplo
En una tabla de empleados:
`DNI -> Nombre`
(Si sé el DNI, sé el Nombre).

## Tipos
*   **Total**: La dependencia es con toda la clave primaria.
*   **Parcial**: La dependencia es solo con una parte de la clave compuesta (viola [Segunda Forma Normal 2FN](Segunda_Forma_Normal_2FN.md)).
*   **Transitiva**: `A -> B` y `B -> C` (viola [Tercera Forma Normal 3FN](Tercera_Forma_Normal_3FN.md)).

---
[00 MOC Normalizacion](00_MOC_Normalizacion.md)
