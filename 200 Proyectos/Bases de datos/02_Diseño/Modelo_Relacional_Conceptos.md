# Modelo Relacional: Conceptos

El **Modelo Relacional** se basa en la teoría matemática de conjuntos. Todos los datos se representan en **Tablas** (relaciones).

## Elementos
*   **Tabla (Relación)**: Conjunto de datos organizados en filas y columnas. Corresponde a una [Entidad](Entidad.md).
*   **Tupla (Fila)**: Representa un registro único.
*   **Atributo (Columna)**: Representa una propiedad. Corresponde a un [Atributo](Atributo.md).
*   **Dominio**: Conjunto de valores válidos para un atributo (ej. enteros, fechas).

## Claves
Para garantizar la integridad, se usan claves:
*   [Clave_Primaria](Clave_Primaria.md)
*   [Clave_Foranea](Clave_Foranea.md)


## Relación con otros conceptos
*   **Implementación**: Este modelo se implementa mediante [SQL_DDL](../03_SQL/SQL_DDL.md) (creación de tablas) y [SQL_DML](../03_SQL/SQL_DML.md) (manipulación).
*   **Teoría**: Las operaciones sobre estas tablas se definen en el [Algebra_Relacional_Concepto](../06_Algebra_Relacional/Algebra_Relacional_Concepto.md).
*   **Optimización**: El diseño de las tablas se refina mediante la [Normalizacion_Objetivos](../04_Normalizacion/Normalizacion_Objetivos.md).

---
[00_MOC_Diseño](00_MOC_Dise%C3%B1o.md)
