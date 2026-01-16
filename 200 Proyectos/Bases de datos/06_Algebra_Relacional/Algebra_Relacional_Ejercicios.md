---
tags: [exercises, relational-algebra, theory]
moc: [[00_MOC_Algebra_Relacional]]
status: refined
difficulty: intermediate
---

# Ejercicios: Álgebra Relacional

---

## 🧠 Núcleo de la Práctica

La resolución de ejercicios de Álgebra Relacional requiere traducir requisitos en lenguaje natural a operaciones matemáticas sobre conjuntos de datos.

*   **Identificar Origen**: Determinar qué relaciones (tablas) contienen los datos necesarios.
*   **Filtrar Primero**: Aplicar [Seleccion Operador](Seleccion_Operador.md) lo antes posible para reducir el volumen de datos.
*   **Reducir Esquema**: Usar [Proyeccion Operador](Proyeccion_Operador.md) para quedarte solo con las columnas solicitadas.

---

## 📝 Casos Prácticos

### 1. Selección y Proyección
**Enunciado**: Obtener el nombre de todos los alumnos que tienen más de 20 años.
> $$\pi\{Nombre\}(\sigma\{Edad > 20\}(Alumnos))$$

### 2. Reunión (Join)
**Enunciado**: Obtener el nombre de los alumnos y el código de los cursos en los que están matriculados.
> $$\pi\{Nombre, Cod\_C\}(Alumnos \bowtie Matricula)$$

### 3. Diferencia (Conjuntos Complementarios)
**Enunciado**: Obtener los DNI de los alumnos que NO se han matriculado en ningún curso.
> $$\pi\{DNI\}(Alumnos) - \pi\{DNI\_A\}(Matricula)$$

### 4. Intersección (Coincidencias)
**Enunciado**: Obtener los DNI de alumnos que están en el curso 'C1' y también en el 'C2'.
> $$\pi\{DNI\_A\}(\sigma\{Cod\_C='C1'\}(Matricula)) \cap \pi\{DNI\_A\}(\sigma\{Cod\_C='C2'\}(Matricula))$$

---

## 🔗 Conexiones y Contexto

*   **Teoría base:** [Algebra Relacional Concepto](Algebra_Relacional_Concepto.md).
*   **Siguiente paso:** [SQL DML](../03_SQL/SQL_DML.md) para implementar estas consultas en una base de datos real.

---

> [!tip] Idea Fuerza (Cierre)
> Dominar el álgebra relacional te permite diseñar cualquier consulta compleja sin perderte en la sintaxis de SQL.

---

## 🗺️ Mapa de Contenido
*   Volver al: [00 MOC Algebra Relacional](00_MOC_Algebra_Relacional.md).
