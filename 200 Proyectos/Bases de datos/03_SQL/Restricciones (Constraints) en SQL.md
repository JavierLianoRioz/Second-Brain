# Restricciones (Constraints) en SQL

Las **restricciones** son reglas que se definen en las columnas de una tabla para limitar el tipo de datos que pueden ser almacenados y garantizar la precisión e [[Integridad Referencial|integridad]] de la información.

Se definen al crear o modificar una tabla con [[DDL (Data Definition Language)]].

### Tipos de Restricciones

*   `PRIMARY KEY`: Define la [[Clave Primaria (PK)]].
*   `FOREIGN KEY`: Define una [[Clave Foránea (FK)]].
*   `NOT NULL`: La columna no puede contener valores nulos.
*   `UNIQUE`: Todos los valores de la columna deben ser diferentes.
*   `CHECK`: Valida que los valores cumplan una condición específica (e.g., `edad > 18`).

---
**Relacionado:** [[DDL (Data Definition Language)]], [[Clave Primaria (PK)]], [[Clave Foránea (FK)]]
