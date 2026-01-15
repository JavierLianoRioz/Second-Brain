# Ejercicios: Álgebra Relacional

Practica la conversión de consultas naturales a expresiones algebraicas.

## Esquema de Datos
- **Alumnos** (DNI, Nombre, Edad)
- **Matricula** (DNI_A, Cod_C, Nota)
- **Cursos** (Cod_C, Nombre_C, Creditos)

---

### Ejercicio 1: Selección y Proyección
**Enunciado**: Obtener el Nombre de todos los alumnos que tienen más de 20 años.
- **Expresión**: $\pi\{Nombre\}(\sigma\{Edad > 20\}(Alumnos))$

### Ejercicio 2: Join Natural
**Enunciado**: Obtener el nombre de los alumnos y el código de los cursos en los que están matriculados.
- **Expresión**: $\pi\{Nombre, Cod\_C\}(Alumnos \bowtie Matricula)$

### Ejercicio 3: Diferencia (Resto)
**Enunciado**: Obtener los DNI de los alumnos que NO se han matriculado en ningún curso.
- **Expresión**: $\pi\{DNI\}(Alumnos) - \pi\{DNI\_A\}(Matricula)$

### Ejercicio 4: Intersección (Usuarios en común)
**Enunciado**: Obtener los DNI de alumnos que están en el curso 'C1' y también en el 'C2'.
- **Expresión**: $\pi\{DNI\_A\}(\sigma\{Cod\_C='C1'\}(Matricula)) \cap \pi\{DNI\_A\}(\sigma\{Cod\_C='C2'\}(Matricula))$

---
[MOC Algebra Relacional](00_MOC_Algebra_Relacional.md)
