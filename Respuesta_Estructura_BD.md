# Estructura de los Apuntes de Base de Datos

Has observado correctamente que hay conceptos y comandos que parecen repetirse o presentarse en diferentes "niveles" dentro de `200 Proyectos\Bases de datos\`. Esto se debe a que los apuntes siguen una **estructura progresiva de aprendizaje**, donde se profundiza en los temas capa por capa.

Aquí te explico cómo están organizados esos niveles:

## 1. Nivel Conceptual (Fundamentos)
**Carpetas:** `01_Introduccion`, `02_Diseño`

*   **Qué es:** Aquí no se ven comandos de código todavía. Se explican los **conceptos teóricos** necesarios para entender qué es una base de datos y cómo se planea antes de tocar el ordenador.
*   **Ejemplo:** Se define qué es una "Clave Primaria" (PK) conceptualmente, pero no cómo se escribe en código.

## 2. Nivel Práctico y Sintaxis (El Lenguaje)
**Carpeta:** `03_SQL`

*   **Qué es:** Este es el nivel de **ejecución**. Aquí se introducen los comandos reales que le das a la máquina.
*   **La "Repetición":** Verás que SQL se divide en sub-lenguajes (DDL, DML, TCL).
    *   **DDL:** Comandos para crear estructuras (`CREATE`, `ALTER`).
    *   **DML:** Comandos para manipular datos (`SELECT`, `INSERT`).
    *   **TCL:** Comandos para controlar transacciones (`COMMIT`, `ROLLBACK`).
*   Aquí aprendes **cómo escribir** el comando.

## 3. Nivel Teórico Profundo (El Porqué)
**Carpetas:** `04_Normalizacion`, `05_Transacciones`, `06_Algebra_Relacional`

*   **Qué es:** Aquí se vuelve a la teoría, pero a un nivel mucho más avanzado para explicar **por qué** funcionan los comandos del nivel anterior.
*   **El caso de las Transacciones:**
    *   En el **Nivel 2 (`03_SQL`)**, aprendiste que existen comandos TCL como `COMMIT` o `ROLLBACK`.
    *   En el **Nivel 3 (`05_Transacciones`)**, se explica la **teoría ACID** que hay detrás. No solo te enseña a escribir `COMMIT`, sino que te explica las reglas de "Atomicidad" y "Consistencia" que hacen que ese comando sea seguro.
*   **El caso del Álgebra Relacional:**
    *   En `03_SQL` aprendes `SELECT ... WHERE`.
    *   En `06_Algebra_Relacional` aprendes la matemática (`σ` Selección) que ocurre internamente cuando ejecutas ese `WHERE`.

---

### Resumen
No son comandos distintos, son **mismos conceptos vistos desde perspectivas diferentes**:
1.  **Diseño:** La idea.
2.  **SQL:** La herramienta práctica.
3.  **Teoría:** La lógica interna.

### Tabla Resumen de Niveles

| Nivel | Carpetas Relacionadas | Enfoque Principal | Ejemplo Concreto |
| :--- | :--- | :--- | :--- |
| **1. Conceptual** | `01_Introduccion`<br>`02_Diseño` | **El Qué**<br>Fundamentos, historia y diseño lógico antes de programar. | Definición de *Clave Primaria (PK)* y *Modelo Entidad-Relación*. |
| **2. Práctico** | `03_SQL` | **El Cómo**<br>Sintaxis, comandos y ejecución directa en el SGBD. | Escribir `CREATE TABLE` o `SELECT * FROM`. |
| **3. Teórico Profundo** | `04_Normalizacion`<br>`05_Transacciones`<br>`06_Algebra_Relacional` | **El Porqué**<br>Matemáticas, reglas de optimización y consistencia interna. | *Propiedades ACID* (detrás de una transacción) o *Selección σ* (detrás de un `WHERE`). |

### Comparativa de Sublenguajes de SQL

| Sublenguaje | Nombre Completo              | Propósito Principal                                              | Comandos Clave                         | ¿Transaccional? (ROLLBACK)                 |
| :---------- | :--------------------------- | :--------------------------------------------------------------- | :------------------------------------- | :----------------------------------------- |
| **DDL**     | Data Definition Language     | Definir y gestionar la estructura de la base de datos (esquema). | `CREATE`, `ALTER`, `DROP`, `TRUNCATE`  | Generalmente NO (cambios permanentes)      |
| **DML**     | Data Manipulation Language   | Manipular los datos dentro de las tablas.                        | `SELECT`, `INSERT`, `UPDATE`, `DELETE` | SÍ (pueden ser revertidos)                 |
| **DCL**     | Data Control Language        | Controlar los permisos y la seguridad de acceso a los datos.     | `GRANT`, `REVOKE`                      | Generalmente NO (efecto inmediato)         |
| **TCL**     | Transaction Control Language | Gestionar y controlar las transacciones DML.                     | `COMMIT`, `ROLLBACK`, `SAVEPOINT`      | N/A (su función es controlar la reversión) |

### Evolución de Comandos SQL a Través de los Niveles

Esta tabla ilustra cómo un comando específico de SQL, aprendido en el nivel práctico, se fundamenta en conceptos previos y se explica en profundidad con principios teóricos posteriores.

| Comando SQL (Nivel Práctico - `03_SQL`) | Concepto Subyacente (Nivel Conceptual - `01_Introduccion`, `02_Diseño`) | Principio Teórico/Profundo (Nivel Teórico Profundo - `04`, `05`, `06`) |
| :------------------------------------- | :--------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| `CREATE TABLE`                         | Entidad, Atributo, Clave Primaria, Clave Foránea                       | Normalización (1FN, 2FN, 3FN), Modelo Relacional                       |
| `ALTER TABLE ... ADD COLUMN`           | Atributo, Esquema                                                      | Normalización (Refactorización de esquema)                             |
| `SELECT ... WHERE`                     | Consulta de Datos, Filtrado, Proyección                                | Álgebra Relacional (Selección `σ`, Proyección `π`)                     |
| `INSERT INTO`                          | Adición de Datos, Tupla                                                | Integridad Referencial, Restricciones (NOT NULL, UNIQUE, CHECK)        |
| `UPDATE`                               | Modificación de Datos                                                  | Integridad de Datos, Consistencia (ACID)                               |
| `DELETE FROM`                          | Eliminación de Datos                                                   | Integridad de Datos, Atomicidad (ACID)                                 |
| `COMMIT` / `ROLLBACK`                  | Transacción                                                            | Propiedades ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad)  |
| `GRANT` / `REVOKE`                     | Permisos, Seguridad                                                    | Control de Acceso                                                      |


