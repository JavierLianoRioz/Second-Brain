---
tags: [sql, dml, exam-prep]
moc: [[00_MOC_SQL]]
status: refined
difficulty: basic
---

# SQL DML: Manipulación de Datos

---

## 🧠 Núcleo del Concepto

El **DML** (Data Manipulation Language) es el subconjunto de SQL responsable de la interacción directa con los datos almacenados en las tablas.

> [!IMPORTANT]
> **TEMA CLAVE EXAMEN FINAL**: El dominio de DML es esencial para cualquier operación CRUD (Create, Read, Update, Delete).

*   **Alcance:** No altera la estructura (DDL), solo el contenido de las filas.
*   **Transaccionalidad:** Las operaciones DML suelen estar sujetas a control de transacciones (`COMMIT`/`ROLLBACK`).
*   **Filtrado:** Casi todos los comandos DML requieren una cláusula `WHERE` para evitar modificaciones masivas accidentales.

---

## 🗺️ Anclaje Visual (Dual Coding)

> [!abstract] Operaciones CRUD vs DML
> 
> | Operación CRUD | Comando SQL | Descripción |
> | :--- | :--- | :--- |
> | **C**reate | [[INSERT]] | Añade nuevas filas a una tabla. |
> | **R**ead | [[SELECT_Basico]] | Recupera y visualiza información. |
> | **U**pdate | [[UPDATE]] | Modifica valores existentes. |
> | **D**elete | [[DELETE]] | Elimina filas de forma permanente. |

---

## 🔗 Conexiones y Contexto

*   **Se basa en:** [[Algebra_Relacional_Concepto]] (la teoría detrás de la selección y manipulación).
*   **Diferencia clave con:** [[SQL_DDL]], que define las tablas; DML solo las "rellena" o modifica.

---

> [!tip] Idea Fuerza (Cierre)
> Si DDL construye el escenario, DML es el conjunto de actores que mueven los datos durante la función.

---

## 🗺️ Mapa de Contenido
*   Para explorar cada comando: [[00_MOC_SQL]].
