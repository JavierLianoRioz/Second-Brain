# Solución Experta: Examen Parcial 2

> **Nota del Profesor:** Esta corrección es estricta. En un examen real, la ambigüedad se penaliza. Presta atención a los detalles técnicos.

---

## 1. Teoría (Tipo Test)

| # | Respuesta | Explicación Técnica |
| :--- | :---: | :--- |
| **1** | **c) `ALTER TABLE`** | `INSERT`/`UPDATE` manipulan datos (DML). `SELECT` es DQL (Query) o DML según el autor. `ALTER` define estructura (DDL). |
| **2** | **b) Dep. Funcional Completa** | La 2FN elimina las dependencias parciales. Si $A \rightarrow B$ y $A$ es parte de la PK, viola 2FN. |
| **3** | **c) Indivisibilidad** | Atomicidad no es persistencia (Durabilidad) ni aislamiento. Es la garantía de "todo o nada". |
| **4** | **b) Dep. Multivaluadas** | La 4FN trata sobre $A \twoheadrightarrow B$. Las dependencias transitivas son de 3FN. |

---

## 2. SQL DDL (Diseño Físico)

### Errores Comunes a Evitar:
*   Usar `FLOAT` para dinero (pérdida de precisión). Usar siempre `DECIMAL` o `NUMERIC`.
*   Olvidar las restricciones `NOT NULL` en campos obligatorios lógicos (como el nombre).
*   No definir la longitud de los `VARCHAR`.

```sql
-- Tabla EMPLEADOS
CREATE TABLE EMPLEADOS (
    id_emp INT AUTO_INCREMENT PRIMARY KEY, -- O SERIAL en Postgres
    dni VARCHAR(20) NOT NULL UNIQUE,       -- UNIQUE implica índice
    nombre VARCHAR(100) NOT NULL,
    salario DECIMAL(10, 2) NOT NULL,
    CONSTRAINT chk_salario_minimo CHECK (salario > 1000)
);

-- Tabla PROYECTOS
CREATE TABLE PROYECTOS (
    id_proy INT PRIMARY KEY,
    nombre_proy VARCHAR(100),
    fecha_inicio DATE DEFAULT (CURRENT_DATE) -- Paréntesis a veces requeridos
);

-- Tabla ASIGNACIONES
CREATE TABLE ASIGNACIONES (
    id_emp INT,
    id_proy INT,
    horas INT NOT NULL, -- Las horas no deberían ser nulas
    
    -- Clave Primaria Compuesta (Obligatorio definirla así)
    CONSTRAINT pk_asignaciones PRIMARY KEY (id_emp, id_proy),
    
    -- FK Empleados: Borrado en Cascada
    CONSTRAINT fk_asig_emp FOREIGN KEY (id_emp) 
        REFERENCES EMPLEADOS(id_emp) 
        ON DELETE CASCADE,
        
    -- FK Proyectos: Restrict (Comportamiento por defecto)
    -- Si intentas borrar un proyecto con asignaciones, fallará.
    CONSTRAINT fk_asig_proy FOREIGN KEY (id_proy) 
        REFERENCES PROYECTOS(id_proy)
        -- ON DELETE RESTRICT (Implícito)
);
```

---

## 3. Normalización Avanzada

### Ejercicio A: 4FN (Dependencias Multivaluadas)

**1. Identificación Formal:**
Existen dos Dependencias Multivaluadas (MVD) independientes en la relación `R(Curso, Profesor, Libro)`:
*   $Curso \twoheadrightarrow Profesor$
*   $Curso \twoheadrightarrow Libro$

**Justificación:** Para un curso dado (ej. 'BD'), el conjunto de profesores asociados (Juan, Ana) aparece combinado con *cada uno* de los libros asociados (SQL, Data). Esto genera redundancia multiplicativa ($N_{prof} \times M_{libros}$ filas).

**2. Descomposición (4FN):**
Debemos separar las MVD independientes en tablas distintas.

*   **R1 (Curso, Profesor)**
    *   PK: (Curso, Profesor)
*   **R2 (Curso, Libro)**
    *   PK: (Curso, Libro)

> **Corrección:** Si dejasteis las tablas unidas, tenéis un 0. La redundancia es inaceptable en 4FN.

### Ejercicio B: 5FN (Dependencias de Join)

**1. Definición:**
Una **Dependencia de Join (JD)** $(R_1, R_2, ..., R_n)$ sobre una relación $R$ implica que $R$ es igual al join natural de sus proyecciones $R_1, R_2, ..., R_n$. La 5FN exige que toda JD sea implicada por las claves candidatas.

**2. Relación con 4FN:**
Sí. La 4FN es un caso especial de la 5FN donde la descomposición es binaria (en dos tablas). La 5FN generaliza esto a $n$ tablas. Si una tabla está en 5FN, no tiene dependencias de join no triviales, lo que incluye las multivaluadas, por tanto cumple 4FN.

---

## 4. Transacciones

**1. Estado Final:**
*   **Empleado:** Existe 'Carlos'.
*   **Salario:** 1500.

**2. Análisis de la Traza:**
1.  `INSERT`: Se escribe 'Carlos' con 1500 en el log de transacciones (memoria).
2.  `SAVEPOINT`: Se marca un hito.
3.  `UPDATE`: Intenta poner 900. El motor SQL verifica el `CHECK (salario > 1000)`.
    *   **Resultado:** Error de restricción. La sentencia `UPDATE` es abortada.
4.  `ROLLBACK TO`: El sistema deshace cualquier efecto parcial (si lo hubiera) hasta el punto `sp_antes_update`.
    *   **Efecto:** Estamos en el estado post-INSERT.
5.  `COMMIT`: Se hacen persistentes los cambios pendientes (el INSERT).

> **Ojo:** Si el error hubiera sido grave (ej. fallo de red o deadlock), el SGBD podría haber abortado *toda* la transacción, haciendo inútil el `ROLLBACK TO`. Pero en errores de restricción lógica, el estándar permite recuperación parcial.
