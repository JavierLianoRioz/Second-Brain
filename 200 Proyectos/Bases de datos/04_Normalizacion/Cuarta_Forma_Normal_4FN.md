# Cuarta Forma Normal (4FN)

## Regla
Una tabla está en **4FN** si:
1.  Cumple con [Tercera_Forma_Normal_3FN](Tercera_Forma_Normal_3FN.md).
2.  No existen **[Dependencia_Multivaluada](Dependencia_Multivaluada.md)** independientes.

## Ejemplo Violación
Un `Profesor` enseña `Materias` y practica `Deportes`.
Si guardamos todo junto: `(Profesor, Materia, Deporte)`, se genera un producto cartesiano innecesario si Materia y Deporte no tienen relación.

## Solución
Separar en dos tablas independientes:
1.  `Docencia (Profesor, Materia)`
2.  `Aficiones (Profesor, Deporte)`

---
[00_MOC_Normalizacion](00_MOC_Normalizacion.md)
