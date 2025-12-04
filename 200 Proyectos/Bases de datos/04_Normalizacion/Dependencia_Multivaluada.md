# Dependencia Multivaluada (MVD)

Una **Dependencia Multivaluada** ocurre cuando un atributo determina un **conjunto de valores** de otro atributo, independientemente de otros atributos en la misma tabla.

## Notación
Se denota con una doble flecha:
$$ A \twoheadrightarrow B $$
Se lee: "A multidetermina a B" o "B es multidependiente de A".

## Definición Formal
En una relación $R(A, B, C)$, existe una MVD $A \twoheadrightarrow B$ si y solo si el conjunto de valores de $B$ asociados a un par $(A, C)$ depende **únicamente** de $A$ y es independiente de $C$.

Esto implica que $A$ y $B$ están relacionados, pero la presencia de $C$ no afecta esa relación. Si existen múltiples valores de $B$ para un $A$, y múltiples valores de $C$ para ese mismo $A$, la tabla debe contener el **Producto Cartesiano** de esos valores para mantener la consistencia.

## Ejemplo
Imagina una tabla `Cursos_Profesores_Libros`:
*   Un `Curso` tiene varios `Profesores`.
*   Un `Curso` tiene varios `Libros` recomendados.
*   Los libros no dependen del profesor.

Si `Base de Datos` lo imparten `Juan` y `Ana`, y los libros son `SQL` y `Teoría`:

| Curso | Profesor | Libro |
| :--- | :--- | :--- |
| BD | Juan | SQL |
| BD | Juan | Teoría |
| BD | Ana | SQL |
| BD | Ana | Teoría |

Aquí:
*   `Curso ->> Profesor`
*   `Curso ->> Libro`

La existencia de estas dependencias en la misma tabla genera redundancia (filas repetidas). La [[Cuarta_Forma_Normal_4FN]] obliga a separarlas.

---
[[00_MOC_Normalizacion]]
