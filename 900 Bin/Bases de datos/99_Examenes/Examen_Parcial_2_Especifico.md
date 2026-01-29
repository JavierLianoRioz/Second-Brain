# Examen Parcial 2 - Ajustado (Revisión Experta)

**Temario:** SQL Avanzado, Normalización (2FN-5FN), Transacciones.
**Nivel:** Intermedio-Alto.

---

## Parte 1: Tipo Test (Teoría)

**1. ¿Cuál de las siguientes sentencias pertenece estrictamente al DDL (Data Definition Language)?**
a) `INSERT INTO`
b) `UPDATE`
c) `ALTER TABLE`
d) `SELECT`

**2. Para que una tabla se encuentre en 2FN, debe cumplir 1FN y además:**
a) No tener dependencias transitivas (Atributo no clave -> Atributo no clave).
b) Todo atributo no clave debe tener dependencia funcional completa de la Clave Primaria.
c) No tener dependencias multivaluadas.
d) La Clave Primaria debe ser un único atributo (simple).

**3. En el contexto ACID, la "Atomicidad" implica que:**
a) Los datos persisten en disco tras un fallo de energía.
b) Las transacciones concurrentes no ven los cambios intermedios de otras.
c) Una transacción es una unidad indivisible: se confirma todo o se deshace todo.
d) La base de datos mantiene la integridad referencial en todo momento.

**4. La 4FN (Cuarta Forma Normal) aísla y elimina:**
a) Dependencias Funcionales Transitivas.
b) Dependencias Multivaluadas (MVD) independientes.
c) Dependencias de Join (JD).
d) Grupos repetitivos y atributos multivaluados simples.

---

## Parte 2: SQL DDL (Diseño Físico)

Escribe las sentencias SQL (estándar o MySQL) para implementar el siguiente esquema, prestando máxima atención a los **tipos de datos** y **restricciones**:

**Escenario: Gestión de Proyectos de Ingeniería**

1.  Tabla **EMPLEADOS**:
    *   `id_emp`: Identificador numérico, Clave Primaria, Autonumérico.
    *   `dni`: Cadena de caracteres (max 20), Único, Obligatorio.
    *   `nombre`: Cadena variable (max 100), Obligatorio.
    *   `salario`: Numérico con 2 decimales. **Restricción**: Debe ser mayor estricto que 1000.

2.  Tabla **PROYECTOS**:
    *   `id_proy`: Identificador numérico, Clave Primaria.
    *   `nombre_proy`: Cadena variable (max 100).
    *   `fecha_inicio`: Fecha. **Valor por defecto**: Fecha del sistema.

3.  Tabla **ASIGNACIONES** (Relación N:M):
    *   Vincula `EMPLEADOS` y `PROYECTOS`.
    *   `horas`: Número entero.
    *   **PK**: La combinación de ambos identificadores.
    *   **Integridad Referencial**:
        *   Si se elimina un empleado, sus asignaciones desaparecen automáticamente.
        *   Si se elimina un proyecto, la operación debe bloquearse si tiene asignaciones.

---

## Parte 3: Normalización (2FN a 5FN)

**Ejercicio A: Análisis de Dependencias (4FN)**
Sea la relación `R(Curso, Profesor, Libro)` con las siguientes reglas de negocio:
*   Un `Curso` es impartido por múltiples `Profesores`.
*   Un `Curso` recomienda múltiples `Libros`.
*   El libro recomendado **no depende** de qué profesor imparta el curso (Independencia de contexto).

**Instancia actual:**

| Curso | Profesor | Libro |
| :--- | :--- | :--- |
| BD | Juan | SQL Guide |
| BD | Juan | Data Models |
| BD | Ana | SQL Guide |
| BD | Ana | Data Models |

1.  Identifica formalmente las Dependencias Multivaluadas (MVD) presentes.
2.  Aplica la descomposición necesaria para alcanzar la **4FN**. Indica las tablas resultantes.

**Ejercicio B: Teoría Avanzada (5FN)**
1.  Define el concepto de **Dependencia de Join (JD)**.
2.  ¿Es cierto que toda relación en 5FN está automáticamente en 4FN? Justifica brevemente.

---

## Parte 4: Control de Transacciones

Analiza la traza de ejecución en un SGBD estándar (ej. PostgreSQL/Oracle) con nivel de aislamiento `READ COMMITTED`:

```sql
-- Tiempo T0
BEGIN TRANSACTION;

-- Tiempo T1
INSERT INTO EMPLEADOS (nombre, salario) VALUES ('Carlos', 1500);

-- Tiempo T2
SAVEPOINT sp_antes_update;

-- Tiempo T3
UPDATE EMPLEADOS SET salario = 900 WHERE nombre = 'Carlos';
-- CONDICIÓN: El CHECK (salario > 1000) salta y produce un ERROR.

-- Tiempo T4
-- (El usuario captura el error y decide restaurar)
ROLLBACK TO sp_antes_update;

-- Tiempo T5
COMMIT;
```

1.  Determina el estado final del empleado 'Carlos' (¿Existe? ¿Salario?).
2.  Justifica tu respuesta basándote en la durabilidad y atomicidad del `SAVEPOINT`.

1.  ¿Qué valor tendrá el salario de 'Carlos' al finalizar?
2.  ¿Se ha guardado el empleado 'Carlos' en la base de datos?

---


